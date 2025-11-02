#!/usr/bin/env python3
"""
Unit tests for Port Scanner project
"""

import sys
import os

# Add the current directory to the path so we can import port_scanner
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from port_scanner import get_open_ports

def test_basic_functionality():
    """Test basic port scanning functionality"""
    print("Testing basic functionality...")
    
    # Test with known host
    result = get_open_ports("scanme.nmap.org", [20, 80])
    assert isinstance(result, list), "Should return a list"
    print("✓ Basic functionality test passed")

def test_verbose_mode():
    """Test verbose mode output"""
    print("Testing verbose mode...")
    
    result = get_open_ports("scanme.nmap.org", [20, 80], True)
    assert isinstance(result, str), "Verbose mode should return string"
    assert "Open ports for" in result, "Should contain header"
    print("✓ Verbose mode test passed")

def test_invalid_hostname():
    """Test error handling for invalid hostname"""
    print("Testing invalid hostname...")
    
    result = get_open_ports("invalidhostname.xyz", [20, 80])
    assert result == "Error: Invalid hostname", "Should return invalid hostname error"
    print("✓ Invalid hostname test passed")

def test_invalid_ip():
    """Test error handling for invalid IP"""
    print("Testing invalid IP...")
    
    result = get_open_ports("999.999.999.999", [20, 80])
    assert result == "Error: Invalid IP address", "Should return invalid IP error"
    print("✓ Invalid IP test passed")

def test_port_range():
    """Test port range scanning"""
    print("Testing port range...")
    
    result = get_open_ports("scanme.nmap.org", [22, 23])
    # At least port 22 (SSH) should be open on scanme.nmap.org
    assert 22 in result, "Port 22 should be open on scanme.nmap.org"
    print("✓ Port range test passed")

def run_tests():
    """Run all tests"""
    try:
        test_basic_functionality()
        test_verbose_mode()
        test_invalid_hostname()
        test_invalid_ip()
        test_port_range()
        print("\n🎉 All tests passed!")
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False

if __name__ == "__main__":
    run_tests()
