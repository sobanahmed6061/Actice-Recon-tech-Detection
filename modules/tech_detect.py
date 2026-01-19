#!/usr/bin/env python3
import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, Style, init
import argparse
import sys

init(autoreset=True)

class TechDetector:
    def __init__(self, target_url, verbose=False):
        self.target_url = target_url if target_url.startswith('http') else f'http://{target_url}'
        self.verbose = verbose
        self.technologies = {
            'server': [],
            'cms': [],
            'frameworks': [],
            'languages': [],
            'analytics': [],
            'cdn': [],
            'misc': []
        }
        
    def log(self, message, level='info'):
        """Logging with verbosity control"""
        if self.verbose or level == 'error':
            timestamp = datetime.now().strftime('%H:%M:%S')
            colors = {'info': Fore.CYAN, 'success': Fore.GREEN, 'error': Fore.RED, 'warning': Fore.YELLOW}
            print(f"[{timestamp}] {colors.get(level, '')}{message}{Style.RESET_ALL}")
    
    def detect_from_headers(self):
        """Detect technologies from HTTP headers"""
        self.log("Analyzing HTTP headers...")
        try:
            response = requests.get(self.target_url, timeout=10, allow_redirects=True, verify=False)
            headers = response.headers
            
            # Server detection
            if 'Server' in headers:
                self.technologies['server'].append(headers['Server'])
                self.log(f"Server: {headers['Server']}", 'success')
            
            # X-Powered-By detection
            if 'X-Powered-By' in headers:
                self.technologies['languages'].append(headers['X-Powered-By'])
                self.log(f"Powered by: {headers['X-Powered-By']}", 'success')
            
            # CDN detection
            cdn_headers = ['CF-RAY', 'X-CDN', 'X-Akamai-Transformed']
            for header in cdn_headers:
                if header in headers:
                    if 'CF-RAY' in header:
                        self.technologies['cdn'].append('Cloudflare')
                    elif 'Akamai' in header:
                        self.technologies['cdn'].append('Akamai')
                    self.log(f"CDN detected: {header}", 'success')
            
            return response.text
            
        except requests.exceptions.RequestException as e:
            self.log(f"Error fetching headers: {e}", 'error')
            return None
    
    def detect_from_html(self, html_content):
        """Detect technologies from HTML content"""
        if not html_content:
            return
        
        self.log("Analyzing HTML content...")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # WordPress detection
        if soup.find('meta', {'name': 'generator', 'content': re.compile('WordPress', re.I)}):
            self.technologies['cms'].append('WordPress')
            self.log("CMS: WordPress detected", 'success')
        
        # Check for wp-content in links
        if soup.find('link', href=re.compile('/wp-content/')):
            if 'WordPress' not in self.technologies['cms']:
                self.technologies['cms'].append('WordPress')
        
        # Joomla detection
        if soup.find('meta', {'name': 'generator', 'content': re.compile('Joomla', re.I)}):
            self.technologies['cms'].append('Joomla')
            self.log("CMS: Joomla detected", 'success')
        
        # Drupal detection
        if soup.find('meta', {'name': 'Generator', 'content': re.compile('Drupal', re.I)}):
            self.technologies['cms'].append('Drupal')
            self.log("CMS: Drupal detected", 'success')
        
        # Framework detection - React
        if 'react' in html_content.lower() or soup.find('div', id='root'):
            self.technologies['frameworks'].append('React')
            self.log("Framework: React detected", 'success')
        
        # Vue.js
        if soup.find(attrs={'v-app': True}) or 'vue' in html_content.lower():
            self.technologies['frameworks'].append('Vue.js')
            self.log("Framework: Vue.js detected", 'success')
        
        # Angular
        if soup.find(attrs={'ng-app': True}) or 'ng-version' in html_content:
            self.technologies['frameworks'].append('Angular')
            self.log("Framework: Angular detected", 'success')
        
        # Bootstrap
        if 'bootstrap' in html_content.lower():
            self.technologies['frameworks'].append('Bootstrap')
        
        # Analytics detection
        if 'google-analytics.com' in html_content or 'gtag' in html_content:
            self.technologies['analytics'].append('Google Analytics')
            self.log("Analytics: Google Analytics detected", 'success')
        
        if 'facebook.com' in html_content and 'fbq' in html_content:
            self.technologies['analytics'].append('Facebook Pixel')
        
        # jQuery
        if 'jquery' in html_content.lower():
            self.technologies['frameworks'].append('jQuery')
    
    def detect_from_cookies(self):
        """Detect technologies from cookies"""
        self.log("Analyzing cookies...")
        try:
            response = requests.get(self.target_url, timeout=10, verify=False)
            cookies = response.cookies
            
            for cookie in cookies:
                # PHP session
                if 'PHPSESSID' in cookie.name:
                    if 'PHP' not in self.technologies['languages']:
                        self.technologies['languages'].append('PHP')
                        self.log("Language: PHP detected (via cookie)", 'success')
                
                # ASP.NET
                if 'ASP.NET' in cookie.name:
                    self.technologies['languages'].append('ASP.NET')
                    self.log("Language: ASP.NET detected (via cookie)", 'success')
                
                # Laravel
                if 'laravel_session' in cookie.name:
                    self.technologies['frameworks'].append('Laravel')
                    self.log("Framework: Laravel detected (via cookie)", 'success')
        
        except Exception as e:
            self.log(f"Error analyzing cookies: {e}", 'error')
    
    def use_wappalyzer(self):
        """Use Wappalyzer library for comprehensive detection"""
        self.log("Running Wappalyzer analysis...")
        try:
            from Wappalyzer import Wappalyzer, WebPage
            
            wappalyzer = Wappalyzer.latest()
            webpage = WebPage.new_from_url(self.target_url)
            detected = wappalyzer.analyze(webpage)
            
            for tech in detected:
                self.technologies['misc'].append(tech)
                self.log(f"Wappalyzer detected: {tech}", 'success')
        
        except Exception as e:
            self.log(f"Wappalyzer analysis failed: {e}", 'warning')
    
    def run_detection(self):
        """Main detection orchestrator"""
        print(f"\n{Fore.YELLOW}{'='*60}")
        print(f"{Fore.YELLOW}Technology Detection for: {self.target_url}")
        print(f"{Fore.YELLOW}{'='*60}\n")
        
        # Run all detection methods
        html_content = self.detect_from_headers()
        self.detect_from_html(html_content)
        self.detect_from_cookies()
        self.use_wappalyzer()
        
        return self.get_results()
    
    def get_results(self):
        """Format and return results"""
        # Remove duplicates
        for category in self.technologies:
            self.technologies[category] = list(set(self.technologies[category]))
        
        return self.technologies
    
    def print_results(self):
        """Pretty print results"""
        results = self.get_results()
        
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.GREEN}DETECTED TECHNOLOGIES")
        print(f"{Fore.GREEN}{'='*60}\n")
        
        categories = {
            'server': 'Web Server',
            'cms': 'Content Management System',
            'frameworks': 'Frameworks & Libraries',
            'languages': 'Programming Languages',
            'analytics': 'Analytics & Tracking',
            'cdn': 'CDN & Hosting',
            'misc': 'Other Technologies'
        }
        
        for key, label in categories.items():
            if results[key]:
                print(f"{Fore.CYAN}{label}:")
                for tech in results[key]:
                    print(f"  • {tech}")
                print()
        
        if not any(results.values()):
            print(f"{Fore.YELLOW}No technologies detected.")
    
    def generate_report(self, output_file='tech_report.txt'):
        """Generate text report"""
        results = self.get_results()
        
        with open(output_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write(f"Technology Detection Report\n")
            f.write(f"Target: {self.target_url}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            categories = {
                'server': 'Web Server',
                'cms': 'Content Management System',
                'frameworks': 'Frameworks & Libraries',
                'languages': 'Programming Languages',
                'analytics': 'Analytics & Tracking',
                'cdn': 'CDN & Hosting',
                'misc': 'Other Technologies'
            }
            
            for key, label in categories.items():
                if results[key]:
                    f.write(f"{label}:\n")
                    for tech in results[key]:
                        f.write(f"  - {tech}\n")
                    f.write("\n")
        
        self.log(f"Report saved to: {output_file}", 'success')

def main():
    parser = argparse.ArgumentParser(description='Technology Detection Module for Recon Tool')
    parser.add_argument('target', help='Target URL or domain')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-o', '--output', help='Output report file', default='reports/tech_report.txt')
    
    args = parser.parse_args()
    
    detector = TechDetector(args.target, verbose=args.verbose)
    detector.run_detection()
    detector.print_results()
    detector.generate_report(args.output)

if __name__ == '__main__':
    main()
