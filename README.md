# Port Scanner Project

A Python-based port scanner that can scan a range of ports on a target hostname or IP address.

## Features

- Scan ports on both hostnames and IP addresses
- Specify custom port ranges
- Verbose mode with service name detection
- Error handling for invalid inputs
- Unit tests for validation

## Files

- `port_scanner.py` - Main port scanner implementation
- `main.py` - Main testing and demonstration script
- `tests/test_module.py` - Unit tests
- `requirements.txt` - Project dependencies (none required)

## Usage

```python
from port_scanner import get_open_ports

# Basic usage - returns list of open ports
open_ports = get_open_ports("scanme.nmap.org", [20, 80])
print(open_ports)

# Verbose mode - returns formatted string
result = get_open_ports("scanme.nmap.org", [20, 80], True)
print(result)
