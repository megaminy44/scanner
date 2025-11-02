import hashlib

def crack_sha1_hash(hash, use_salts=False):
    """
    Crack a SHA-1 hash by comparing against top 10,000 passwords.
    
    Args:
        hash (str): The SHA-1 hash to crack
        use_salts (bool): Whether to use salts from known-salts.txt
    
    Returns:
        str: The cracked password or "PASSWORD NOT IN DATABASE"
    """
    # Read the top 10,000 passwords
    try:
        with open('top-10000-passwords.txt', 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f]
    except FileNotFoundError:
        return "PASSWORD NOT IN DATABASE"
    
    # If using salts, read the known salts
    salts = []
    if use_salts:
        try:
            with open('known-salts.txt', 'r', encoding='utf-8') as f:
                salts = [line.strip() for line in f]
        except FileNotFoundError:
            # If salts file doesn't exist, proceed without salts
            pass
    
    if use_salts and salts:
        # Try each password with each salt (appended and prepended)
        for password in passwords:
            for salt in salts:
                # Prepend salt
                prepended = salt + password
                if hashlib.sha1(prepended.encode()).hexdigest() == hash:
                    return password
                
                # Append salt
                appended = password + salt
                if hashlib.sha1(appended.encode()).hexdigest() == hash:
                    return password
    else:
        # Try each password without salts
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
    
    return "PASSWORD NOT IN DATABASE"

# Test function
if __name__ == "__main__":
    # Test cases from the project description
    test_cases = [
        ("b305921a3723cd5d70a375cd21a61e60aabb84ec", False, "sammy123"),
        ("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e", False, "abacab"),
        ("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", False, "password"),
        ("53d8b3dc9d39f0184144674e310185e41a87ffd5", True, "superman"),
        ("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True, "q1w2e3r4t5"),
        ("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True, "bubbles1")
    ]
    
    print("Testing SHA-1 Password Cracker...")
    print("=" * 50)
    
    for hash_val, use_salts, expected in test_cases:
        result = crack_sha1_hash(hash_val, use_salts)
        status = "✓" if result == expected else "✗"
        print(f"{status} Hash: {hash_val}")
        print(f"   Use Salts: {use_salts}")
        print(f"   Expected: {expected}")
        print(f"   Got: {result}")
        print()
