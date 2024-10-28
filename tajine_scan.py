import socket
import sys
import time
from datetime import datetime
import argparse

def print_banner():
    """
    Display ASCII art banner for Tajine Scan
    """
    banner = """
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
    """
    print(banner)

def educational_port_scan(target_host, start_port, end_port, delay=0.1):
    """
    Educational port scanner that demonstrates basic network security concepts.
    Includes built-in delays and documentation to encourage responsible use.
    
    Args:
        target_host (str): Target hostname or IP (should be your own test system)
        start_port (int): Starting port number
        end_port (int): Ending port number
        delay (float): Delay between scans to prevent network flooding
    """
    print_banner()
    
    print("\n[+] IMPORTANT: This tool is for educational purposes only.")
    print("[+] Only scan systems you own or have explicit permission to test.\n")
    
    # Input validation
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("[-] Error: Could not resolve hostname")
        return
    
    # Start time
    print(f"[*] Target IP: {target_ip}")
    print(f"[*] Scan started at: {datetime.now()}\n")
    
    try:
        # Port scanning loop with educational comments
        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            # Educational output explaining what's happening
            sys.stdout.write(f"\r[*] Scanning port {port}")
            sys.stdout.flush()
            
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"\n[+] Port {port}: Open")
                # Educational information about common ports
                if port in COMMON_PORTS:
                    print(f"    ╰─ Service: {COMMON_PORTS[port]}")
            sock.close()
            
            # Built-in delay to prevent aggressive scanning
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\n[-] Scan interrupted by user.")
        return
    except socket.error:
        print("\n[-] Could not connect to server.")
        return

    # Summary report with educational context
    print("\n" + "="*60)
    print("[+] Scan Summary")
    print("="*60)
    print(f"[*] Target: {target_ip}")
    print(f"[*] Port range: {start_port}-{end_port}")
    print(f"[*] Open ports found: {len(open_ports)}")
    if open_ports:
        print("\n[+] Detailed Results:")
        for port in open_ports:
            print(f"    ╰─ Port {port}")
            if port in COMMON_PORTS:
                print(f"       ╰─ Service: {COMMON_PORTS[port]}")
    print("\n[*] Scan completed at:", datetime.now())

# Common ports dictionary for educational context
COMMON_PORTS = {
    20: "FTP (Data Transfer)",
    21: "FTP (Command Control)",
    22: "SSH (Secure Shell)",
    23: "Telnet (Unencrypted Remote Access)",
    25: "SMTP (Email)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Web Server)",
    443: "HTTPS (Secure Web Server)",
    3306: "MySQL (Database)",
    3389: "RDP (Remote Desktop)",
    8080: "HTTP Alternate (Web Server)",
    27017: "MongoDB (Database)",
    6379: "Redis (Cache Server)",
    5432: "PostgreSQL (Database)"
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tajine Scan - Educational Network Security Scanner"
    )
    parser.add_argument("host", help="Target hostname or IP address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument(
        "--delay", 
        type=float, 
        default=0.1,
        help="Delay between port scans (seconds)"
    )
    
    args = parser.parse_args()
    educational_port_scan(args.host, args.start_port, args.end_port, args.delay)
