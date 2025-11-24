'''Write a program that reads a file containing a list of usernames and passwords, one pair per 
line (separated by a comma). It checks each password to see if it has been leaked in a data breach. 
You can use the "Have I Been Pwned" API (https://haveibeenpwned.com/API/v3) to 
check if a password has been leaked.'''


import hashlib
import requests

def check_password_pwned(password: str) -> int:
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]

    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f'Error fetching from API: {response.status_code}')

    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)

    return 0

def check_passwords_file(filename: str):
    print(f"Reading file: {filename}")
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or ',' not in line:
                continue

            username, password = map(str.strip, line.split(',', 1))
            try:
                count = check_password_pwned(password)
                if count:
                    print(f"[LEAKED] User: {username} - Password found {count} times in breaches.")
                else:
                    print(f"[SAFE] User: {username} - Password not found in breaches.")
            except Exception as e:
                print(f"[ERROR] User: {username} - Could not check password: {e}")

if __name__ == '__main__':
    filename = input("Enter the filename to check: ")
    check_passwords_file(filename)
