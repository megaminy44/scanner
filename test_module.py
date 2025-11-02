#!/usr/bin/env python3
"""
Unit tests for SHA-1 Password Cracker project
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from password_cracker import crack_sha1_hash

def test_crack_no_salts():
    """Test password cracking without salts"""
    print("Testing without salts...")
    
    # Test case 1
    result = crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec")
    assert result == "sammy123", f"Expected 'sammy123', got '{result}'"
    print("✓ Test 1 passed")
    
    # Test case 2
    result = crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")
    assert result == "abacab", f"Expected 'abacab', got '{result}'"
    print("✓ Test 2 passed")
    
    # Test case 3
    result = crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
    assert result == "password", f"Expected 'password', got '{result}'"
    print("✓ Test 3 passed")

def test_crack_with_salts():
    """Test password cracking with salts"""
    print("Testing with salts...")
    
    # Test case 1
    result = crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
    assert result == "superman", f"Expected 'superman', got '{result}'"
    print("✓ Test 1 passed")
    
    # Test case 2
    result = crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
    assert result == "q1w2e3r4t5", f"Expected 'q1w2e3r4t5', got '{result}'"
    print("✓ Test 2 passed")
    
    # Test case 3
    result = crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)
    assert result == "bubbles1", f"Expected 'bubbles1', got '{result}'"
    print("✓ Test 3 passed")

def test_password_not_in_database():
    """Test handling of passwords not in database"""
    print("Testing non-existent passwords...")
    
    # Random SHA-1 hash that shouldn't match anything
    fake_hash = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
    result = crack_sha1_hash(fake_hash)
    assert result == "PASSWORD NOT IN DATABASE", f"Expected 'PASSWORD NOT IN DATABASE', got '{result}'"
    print("✓ Test passed")

def run_all_tests():
    """Run all test cases"""
    print("Running SHA-1 Password Cracker Tests")
    print("=" * 40)
    
    try:
        test_crack_no_salts()
        test_crack_with_salts()
        test_password_not_in_database()
        print("\n🎉 All tests passed!")
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False

if __name__ == "__main__":
    run_all_tests()
