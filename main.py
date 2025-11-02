#!/usr/bin/env python3
"""
Main testing file for Port Scanner project
"""

# Import the function directly from port_scanner
from port_scanner import get_open_ports

def main():
    print("Port Scanner Project - Main Test File")
    print("=" * 40)
    
    # Manual test cases
    test_cases = [
        ("scanme.nmap.org", [20, 80]),
        ("google.com", [79, 82]),
        ("127.0.0.1", [80, 85])
    ]
    
    for target, port_range in test_cases:
        print(f"\nScanning {target} on ports {port_range[0]}-{port_range[1]}:")
        try:
            result = get_open_ports(target, port_range)
            print(f"Open ports: {result}")
            
            # Test verbose mode
            verbose_result = get_open_ports(target, port_range, True)
            print("Verbose mode:")
            print(verbose_result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
