# SHA-1 Password Cracker

A Python-based password cracker that can crack SHA-1 hashes by comparing against common passwords.

## Features

- Crack SHA-1 hashes using a database of common passwords
- Support for salted passwords (prepending and appending salts)
- Comprehensive test suite
- Error handling for passwords not in database

## Files

- `password_cracker.py` - Main password cracker implementation
- `top-10000-passwords.txt` - Common passwords database
- `known-salts.txt` - Common salts used for password hashing
- `main.py` - Main testing and demonstration script
- `test_module.py` - Unit tests
- `requirements.txt` - Project dependencies (none required)

## Usage

```python
from password_cracker import crack_sha1_hash

# Crack without salts
password = crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec")
print(password)  # Returns "sammy123"

# Crack with salts
password = crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
print(password)  # Returns "superman"
