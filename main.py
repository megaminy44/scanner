#!/usr/bin/env python3
"""
Main testing file for SHA-1 Password Cracker project
"""

from password_cracker import crack_sha1_hash

def main():
    print("SHA-1 Password Cracker - Test Suite")
    print("=" * 50)
    
    # Test cases without salts
    print("\n1. Testing without salts:")
    print("-" * 30)
    
    test_cases_no_salt = [
        ("b305921a3723cd5d70a375cd21a61e60aabb84ec", "sammy123"),
        ("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e", "abacab"),
        ("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", "password")
    ]
    
    for hash_val, expected in test_cases_no_salt:
        result = crack_sha1_hash(hash_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {hash_val}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()
    
    # Test cases with salts
    print("\n2. Testing with salts:")
    print("-" * 30)
    
    test_cases_salt = [
        ("53d8b3dc9d39f0184144674e310185e41a87ffd5", "superman"),
        ("da5a4e8cf89539e66097acd2f8af128acae2f8ae", "q1w2e3r4t5"),
        ("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", "bubbles1")
    ]
    
    for hash_val, expected in test_cases_salt:
        result = crack_sha1_hash(hash_val, use_salts=True)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {hash_val}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()
    
    # Test case that should fail
    print("\n3. Testing non-existent password:")
    print("-" * 30)
    
    fake_hash = "a" * 40  # Random SHA-1 hash
    result = crack_sha1_hash(fake_hash)
    print(f"Hash: {fake_hash}")
    print(f"Result: {result}")
    print(f"Status: {'PASS' if result == 'PASSWORD NOT IN DATABASE' else 'FAIL'}")

if __name__ == "__main__":
    main()
