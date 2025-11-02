import socket

# Common ports dictionary included directly in the file
common_ports = {
    21: "ftp",
    22: "ssh", 
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    115: "sftp",
    135: "rpc",
    139: "netbios",
    143: "imap",
    194: "irc",
    443: "https",
    445: "microsoft-ds",
    1433: "ms-sql",
    3306: "mysql",
    3389: "rdp",
    5432: "postgresql",
    5900: "vnc",
    6379: "redis",
    27017: "mongodb"
}

def is_valid_ip(ip):
    """Check if the given string is a valid IP address"""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def resolve_hostname(hostname):
    """Resolve hostname to IP address, return None if invalid"""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    
    # Determine if target is IP or hostname and validate
    if is_valid_ip(target):
        ip_address = target
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            hostname = None
    else:
        # Try to resolve hostname
        ip_address = resolve_hostname(target)
        if ip_address is None:
            return "Error: Invalid hostname"
        hostname = target
    
    # Validate IP address
    if not is_valid_ip(ip_address):
        return "Error: Invalid IP address"
    
    # Scan ports in the specified range
    start_port, end_port = port_range
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        
        try:
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
        except:
            pass
        finally:
            sock.close()
    
    # Return based on verbose mode
    if not verbose:
        return open_ports
    else:
        # Build verbose output
        if hostname:
            output = f"Open ports for {hostname} ({ip_address})\n"
        else:
            output = f"Open ports for {ip_address}\n"
        
        output += "PORT     SERVICE\n"
        
        for port in open_ports:
            service_name = common_ports.get(port, "unknown")
            output += f"{port:<8} {service_name}\n"
        
        return output.rstrip()  # Remove trailing newline

# For testing the function directly
if __name__ == "__main__":
    # Test cases
    print("Testing port scanner...")
    result1 = get_open_ports("scanme.nmap.org", [20, 80])
    print(f"Scanme.nmap.org [20-80]: {result1}")
    
    result2 = get_open_ports("scanme.nmap.org", [20, 80], True)
    print("\nVerbose mode:")
    print(result2)
