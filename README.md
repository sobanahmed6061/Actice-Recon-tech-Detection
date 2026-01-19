# Custom Reconnaissance Tool - Technology Detection Module

## 📋 Project Information
**Internship Task:** Offensive Security Tool Development  
**Organization:** ITSOLERA Cyber Department  
**Module:** Active Reconnaissance - Technology Detection  
**Author:** [Soban Ahmed]  
**Date:** 19January 2026

## 🎯 Objective
This module is part of a modular reconnaissance tool designed to detect web technologies, frameworks, CMS, and server configurations during penetration testing engagements.

## ✨ Features

### Technology Detection Capabilities:
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
1. HTTP Header Analysis
2. HTML Content Parsing
3. Cookie Analysis
4. Meta Tag Inspection
5. JavaScript Library Detection
6. External API Integration (Wappalyzer)

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Kali Linux (or any Linux distribution)
- Internet connection

### Setup Instructions

1. **Clone or download the project:**
```bash
cd ~/
mkdir recon-tool
cd recon-tool
```

2. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
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

# Scan your target domain
python3 modules/tech_detect.py example.com -v
```

## 📊 Sample Output
```
============================================================
Technology Detection for: http://testphp.vulnweb.com/
============================================================

============================================================
DETECTED TECHNOLOGIES
============================================================

Web Server:
  • nginx/1.19.0

Programming Languages:
  • PHP/5.6.40-38+ubuntu20.04.1+deb.sury.org+1
```

## 📁 Project Structure
```
recon-tool/
├── modules/
│   ├── __init__.py
│   └── tech_detect.py       # Technology detection module
├── reports/                  # Generated reports stored here
│   └── tech_report.txt
├── logs/                     # Log files (future implementation)
├── venv/                     # Virtual environment
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔧 Command-Line Arguments

| Argument | Short | Description | Required |
|----------|-------|-------------|----------|
| target | - | Target URL or domain | Yes |
| --verbose | -v | Enable verbose output | No |
| --output | -o | Output report filename | No |

## 🛠️ Technical Details

### Dependencies
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `python-Wappalyzer` - Technology fingerprinting
- `colorama` - Colored terminal output
- `lxml` - XML/HTML processing

### Detection Techniques

1. **Header Analysis:**
   - Server headers
   - X-Powered-By headers
   - CDN-specific headers

2. **HTML Parsing:**
   - Meta generator tags
   - Link references (wp-content, etc.)
   - Script sources
   - Framework-specific attributes

3. **Cookie Analysis:**
   - Session cookies (PHPSESSID, ASP.NET, etc.)
   - Framework cookies (Laravel, etc.)

4. **Content Pattern Matching:**
   - Regular expressions for framework detection
   - Library-specific code patterns

## ⚠️ Legal & Ethical Considerations

**IMPORTANT:** This tool is for educational and authorized testing only.

- ✅ Only scan systems you own or have explicit permission to test
- ✅ Use authorized test sites (testphp.vulnweb.com, etc.)
- ❌ Never scan systems without authorization
- ❌ Unauthorized scanning may be illegal in your jurisdiction

### Recommended Test Sites:
- http://testphp.vulnweb.com
- http://testhtml5.vulnweb.com
- http://testasp.vulnweb.com

## 🔮 Future Enhancements

- [ ] HTML report generation
- [ ] Version detection for frameworks
- [ ] Security header analysis (CSP, HSTS, etc.)
- [ ] Screenshot capture
- [ ] Technology vulnerability mapping
- [ ] Multi-threading for faster scanning
- [ ] JSON output format
- [ ] Database storage of results

## 🤝 Integration with Main Tool

This module is designed to integrate with the main reconnaissance tool:
```python
# Example integration
from modules.tech_detect import TechDetector

detector = TechDetector(target_url, verbose=True)
results = detector.run_detection()
detector.print_results()
detector.generate_report('reports/scan.txt')
```

## 📝 Module Design

### Modularity
- Independent functionality
- Can be called via command-line flags
- Returns structured data for integration
- Logging with verbosity levels

### Code Quality
- Well-documented functions
- Error handling
- Clean separation of concerns
- PEP 8 compliant

## 👥 Team Collaboration

This module is part of a larger group project. Other modules include:
- WHOIS lookup
- DNS enumeration
- Subdomain enumeration
- Port scanning
- Banner grabbing

## 📚 References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Wappalyzer Documentation](https://www.wappalyzer.com/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 📧 Contact

For questions or contributions, please contact:
- **ITSOLERA Cyber Department**
- **Team Lead:** Muhammad Ahsan Ayaz

## 📄 License

This project is created for educational purposes as part of the ITSOLERA Summer Internship Program.

---

**Submission Date:** June 13, 2025  
**Status:** ✅ Completed
