'''Write a program that simulates a brute-force attack on a password by trying out 
all possible character combinations.'''


import itertools
import string
import time

def brute_force_password_verbose(target_password, charset):
    max_length = len(target_password)
    attempts = 0

    for length in range(1, max_length + 1):
        for attempt_tuple in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt_tuple)
            attempts += 1
            print(f"Attempt {attempts}: {attempt}")  
            if attempt == target_password:
                return attempt, attempts
    return None, attempts

if __name__ == "__main__":
    password = input("Enter the password to brute-force: ")
    charset = string.ascii_letters + string.digits 

    print(f"Starting brute-force attack on password of length {len(password)}...")
    start_time = time.time()

    found, total_attempts = brute_force_password_verbose(password, charset)

    end_time = time.time()
    if found:
        print(f"Password found: '{found}' in {total_attempts} attempts.")
    else:
        print("Password not found.")

    print(f"Total time taken: {end_time - start_time:.2f} seconds.")

