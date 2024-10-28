# Tajine Scan 🔍

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Tajine Scan is an educational network security tool designed to help students and security enthusiasts learn about port scanning and network reconnaissance in a safe, controlled environment. This tool is built with education in mind and includes detailed documentation about common network services and security concepts.

## ⚠️ Educational Purpose Only

This tool is designed strictly for educational purposes. Only use it on systems you own or have explicit permission to test. Unauthorized scanning of networks or systems is prohibited and may be illegal in your jurisdiction.

## 🌟 Features

- Educational port scanning with built-in safety features
- Detailed information about common network services
- User-friendly ASCII interface
- Built-in scanning delays to prevent network flooding
- Comprehensive error handling
- Detailed scan reports with service identification

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tajine-scan.git
cd tajine-scan
```

2. No additional dependencies required - uses Python standard library only!

## 📖 Usage

Basic usage:
```bash
python tajine_scan.py [target] [start_port] [end_port] [--delay delay_time]
```

Example scanning localhost ports 1-1024:
```bash
python tajine_scan.py localhost 1 1024
```

Example with custom delay:
```bash
python tajine_scan.py localhost 1 1024 --delay 0.2
```

### Command Line Arguments

- `target`: Hostname or IP address to scan
- `start_port`: First port to scan
- `end_port`: Last port to scan
- `--delay`: Time delay between port scans (default: 0.1 seconds)

## 📋 Sample Output

```
╔════════════════════════════════════════════════════════════════╗
    ___________        _ _                 _____                 
    |__   __/___ _    (_|_)              / ____|                
       | |  / _ (_)    _| |_ __   ___   | (___   ___ __ _ _ __  
       | | |  __/ |   | | | '_ \ / _ \   \___ \ / __/ _` | '_ \ 
       | |  \___| |   | | | | | |  __/   ____) | (_| (_| | | | |
       |_|     |_|   |_|_|_| |_|\___|  |_____/ \___\__,_|_| |_|

    [*] Educational Security Scanner v1.0
    [*] For learning purposes only
    [*] Use responsibly and ethically
╚════════════════════════════════════════════════════════════════╝

[+] Port 80: Open
    ╰─ Service: HTTP (Web Server)
[+] Port 443: Open
    ╰─ Service: HTTPS (Secure Web Server)
```

## 🔍 Common Ports and Services

The scanner includes information about common network services, including:
- FTP (20/21): File Transfer Protocol
- SSH (22): Secure Shell
- HTTP (80): Web Server
- HTTPS (443): Secure Web Server
- MySQL (3306): Database Server
- And many more...

## 🛡️ Security Features

1. Built-in scan delays to prevent aggressive scanning
2. Clear warnings about appropriate usage
3. Educational information about discovered services
4. Timeout controls to prevent hanging
5. User-friendly error messages

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring they comply with all applicable laws and regulations when using this tool. The authors assume no liability for misuse or damage caused by this program.

## 📚 Educational Resources

To learn more about network security and port scanning, check out these resources:
- [NIST Computer Security Resource Center](https://csrc.nist.gov/)
- [OWASP Foundation](https://owasp.org/)
- [Cybersecurity & Infrastructure Security Agency](https://www.cisa.gov/cybersecurity)

## 🔧 Troubleshooting

### Common Issues

1. **Permission Denied Error**
   - Run the script with appropriate permissions
   - Ensure you're scanning allowed targets

2. **Hostname Resolution Error**
   - Check your internet connection
   - Verify the hostname is correct

3. **Slow Scanning**
   - Adjust the delay parameter
   - Check network conditions

## 📮 Contact

For questions, suggestions, or concerns, please open an issue in the GitHub repository.

Remember: Always scan responsibly and ethically!
