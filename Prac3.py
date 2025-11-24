'''Write a program that defines a function and takes a password string as input and 
returns its SHA-256 hashed representation as a hexadecimal string.'''


import hashlib

def hash_password_sha256(password: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    password_input = input("Enter your password: ")
    hashed = hash_password_sha256(password_input)
    print("SHA-256 hashed password (hexadecimal):", hashed)