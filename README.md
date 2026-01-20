# Custom Reconnaissance Tool - Technology Detection Module

## 📋 Project Information
**Internship Task:** Offensive Security Tool Development  
**Organization:** ITSOLERA Cyber Department  
**Module:** Active Reconnaissance - Technology Detection  
**Author:** Soban Ahmed  
**Date:** January 2026

## 🎯 Objective
This module is part of a modular reconnaissance tool designed to detect web technologies, frameworks, CMS, server configurations, **operating systems, and version information** during penetration testing engagements.

## ✨ Features

### Technology Detection Capabilities:
- ✅ **Operating System Detection** (Ubuntu, Debian, CentOS, Windows Server, etc.) **[NEW!]**
- ✅ **Version Extraction** (Server versions, Framework versions, CMS versions) **[NEW!]**
- ✅ **Web Server Detection** (nginx, Apache, IIS, etc.)
- ✅ **Programming Languages** (PHP, Python, ASP.NET, etc.)
- ✅ **CMS Detection** (WordPress, Joomla, Drupal)
- ✅ **JavaScript Frameworks** (React, Vue.js, Angular, jQuery)
- ✅ **CSS Frameworks** (Bootstrap, Tailwind, etc.)
- ✅ **Analytics Tools** (Google Analytics, Facebook Pixel)
- ✅ **CDN Detection** (Cloudflare, Akamai)
- ✅ **Cookie-based Technology Detection**
- ✅ **Integration with Wappalyzer**

### Detection Methods:
1. **HTTP Header Analysis** - Server, OS, and language detection from headers
2. **HTML Content Parsing** - Framework and CMS detection from HTML source
3. **Cookie Analysis** - Technology fingerprinting via cookies
4. **Meta Tag Inspection** - CMS and generator detection
5. **JavaScript Library Detection** - Framework version extraction
6. **Version Extraction** - Precise version numbers for all detected technologies **[NEW!]**
7. **OS Fingerprinting** - Operating system detection from server headers **[NEW!]**
8. **External API Integration** - Wappalyzer for comprehensive coverage

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Kali Linux (or any Linux distribution)
- Internet connection

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/sobanahmed6061/Actice-Recon-tech-Detection.git
cd Actice-Recon-tech-Detection
```

2. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
pip install setuptools  # For Wappalyzer compatibility
```

## 📖 Usage

### Basic Usage
```bash
python3 modules/tech_detect.py <target_url>
```

### With Verbose Output
```bash
python3 modules/tech_detect.py <target_url> -v
```

### Generate Custom Report
```bash
python3 modules/tech_detect.py <target_url> -v -o reports/custom_report.txt
```

### Examples
```bash
# Scan a test website
python3 modules/tech_detect.py http://testphp.vulnweb.com/ -v

# Scan with custom output
python3 modules/tech_detect.py wordpress.org -v -o reports/wordpress_scan.txt

# Scan with OS and version detection
python3 modules/tech_detect.py example.com -v
```

## 📊 Sample Output
```
============================================================
Technology Detection for: http://testphp.vulnweb.com/
============================================================

DETECTED TECHNOLOGIES
============================================================

Operating System:
  • Linux (Ubuntu 20.04.1)

Web Server:
  • nginx

Programming Languages:
  • PHP

Version Information:
  • nginx: 1.19.0
  • PHP: 5.6.40

Other Technologies:
  • DreamWeaver
  • Nginx
  • PHP
  • Ubuntu
```

## 📁 Project Structure
```
Actice-Recon-tech-Detection/
├── modules/
│   ├── __init__.py
│   └── tech_detect.py       # Main technology detection module
├── reports/                  # Generated reports stored here
│   ├── tech_report.txt
│   ├── testphp_updated.txt
│   └── wordpress_updated.txt
├── venv/                     # Virtual environment
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔧 Command-Line Arguments

| Argument | Short | Description | Required |
|----------|-------|-------------|----------|
| target | - | Target URL or domain | Yes |
| --verbose | -v | Enable verbose output with timestamps | No |
| --output | -o | Output report filename | No |

## 🛠️ Technical Details

### Dependencies
- `requests` - HTTP requests and header analysis
- `beautifulsoup4` - HTML parsing and content analysis
- `python-Wappalyzer` - Technology fingerprinting library
- `colorama` - Colored terminal output
- `lxml` - XML/HTML processing
- `setuptools` - Package management

### Detection Techniques

1. **Header Analysis:**
   - Server headers (nginx, Apache, IIS)
   - X-Powered-By headers (PHP, ASP.NET)
   - CDN-specific headers (Cloudflare, Akamai)
   - OS detection from server signatures **[NEW!]**

2. **Version Extraction:** **[NEW!]**
   - Regex-based version parsing from headers
   - HTML source code version detection
   - Framework version identification
   - Precise version numbers for:
     - Web servers (nginx/1.19.0)
     - Languages (PHP/5.6.40)
     - CMS (WordPress 6.1.1)
     - Frameworks (jQuery 3.6.0, Bootstrap 5.2.0)

3. **OS Fingerprinting:** **[NEW!]**
   - Ubuntu version detection
   - Debian, CentOS, Red Hat detection
   - Windows Server detection
   - Generic Linux identification

4. **HTML Parsing:**
   - Meta generator tags
   - Link references (wp-content, etc.)
   - Script sources and versions
   - Framework-specific attributes

5. **Cookie Analysis:**
   - Session cookies (PHPSESSID, ASP.NET)
   - Framework cookies (Laravel, Django)

6. **Content Pattern Matching:**
   - Regular expressions for framework detection
   - Library-specific code patterns
   - Version number extraction

## ⚠️ Legal & Ethical Considerations

**IMPORTANT:** This tool is for educational and authorized testing only.

- ✅ Only scan systems you own or have explicit permission to test
- ✅ Use authorized test sites (testphp.vulnweb.com, etc.)
- ❌ Never scan systems without authorization

### Recommended Test Sites:
- http://testphp.vulnweb.com
- http://testhtml5.vulnweb.com
- http://testasp.vulnweb.com
- https://wordpress.org

## 🔮 Features Implemented

### Core Features (Required):
- [x] HTTP header analysis
- [x] Technology detection
- [x] CMS identification
- [x] Framework detection
- [x] Report generation (TXT format)
- [x] Command-line interface
- [x] Verbose logging
- [x] Wappalyzer integration

### Advanced Features (Bonus):
- [x] **Operating System Detection** 🆕
- [x] **Version Extraction** 🆕
- [x] **Precise Version Numbers** 🆕
- [x] CDN detection
- [x] Analytics tool detection
- [x] Cookie-based fingerprinting
- [x] Color-coded output
- [x] Timestamp logging
- [x] Error handling
- [x] Warning suppression

### Future Enhancements:
- [ ] HTML report generation
- [ ] JSON output format
- [ ] Multi-threading for faster scanning
- [ ] Docker container support
- [ ] GUI interface
- [ ] Database storage of results
- [ ] Vulnerability mapping
- [ ] Screenshot capture

## 🤝 Integration with Main Tool

This module is designed to integrate seamlessly with the main reconnaissance tool:
```python
# Example integration
from modules.tech_detect import TechDetector

# Initialize detector
detector = TechDetector(target_url, verbose=True)

# Run all detections
results = detector.run_detection()

# Display results
detector.print_results()

# Generate report
detector.generate_report('reports/scan.txt')

# Access specific results
os_info = results['os']
versions = results['versions']
servers = results['server']
```

## 📝 Module Design

### Modularity
- Independent functionality - can run standalone
- Command-line flag support (--verbose, --output)
- Returns structured data for easy integration
- Logging with verbosity levels
- Clean separation of concerns

### Code Quality
- Well-documented functions with docstrings
- Comprehensive error handling
- Try-catch blocks for network operations
- Warning suppression for cleaner output
- PEP 8 compliant code style
- Regex patterns for robust detection

### Architecture
```
TechDetector Class
├── __init__()              # Initialize detector
├── detect_from_headers()   # Header analysis
├── detect_from_html()      # HTML parsing
├── detect_from_cookies()   # Cookie analysis
├── detect_os_from_headers() # OS detection [NEW]
├── extract_versions()      # Version extraction [NEW]
├── use_wappalyzer()       # External API
├── run_detection()        # Main orchestrator
├── print_results()        # Display output
└── generate_report()      # Report generation
```

## 👥 Team Collaboration

This module is part of a larger group project. Other modules include:
- **WHOIS Lookup** - Domain registration info
- **DNS Enumeration** - DNS records (A, MX, TXT, NS)
- **Subdomain Enumeration** - Subdomain discovery
- **Port Scanning** - Open port detection
- **Banner Grabbing** - Service identification

### Integration Benefits:
- Consistent CLI interface across modules
- Unified report format
- Modular architecture for easy maintenance
- Independent operation capability
- Structured data output for aggregation

## 📚 References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Wappalyzer Documentation](https://www.wappalyzer.com/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [WhatWeb Tool](https://github.com/urbanadventurer/WhatWeb)

## 🎓 Learning Outcomes

### Technical Skills Gained:
- Python programming and scripting
- Web scraping and HTML parsing
- HTTP protocol understanding
- Regular expressions for pattern matching
- Version control with Git/GitHub
- Command-line tool development
- API integration (Wappalyzer)
- Error handling and debugging

### Professional Skills:
- Technical documentation writing
- Code organization and modularization
- Project management
- Team collaboration
- Version control workflows
- Security tool development

## 📄 License

This project is created for educational purposes as part of the ITSOLERA  Internship Program 2026.

