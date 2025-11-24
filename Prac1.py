'''Write a program to perform encryption and decryption using Caesar cipher (substitutional cipher).'''


def encrypt_caesar(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

if __name__ == "__main__":
    choice = input("Choose operation (encrypt/decrypt) by typing 'e' or 'd': ").strip().lower()

    if choice not in ["e", "d"]:
        print("Invalid operation. Please enter 'e' or 'd'.")
    else:
        message = input("Enter the message: ")
        try:
            key = int(input("Enter the key (shift amount, integer): "))
            if choice == "e":
                encrypted = encrypt_caesar(message, key)
                print("Encrypted message:", encrypted)
            else:
                decrypted = decrypt_caesar(message, key)
                print("Decrypted message:", decrypted)
        except ValueError:
            print("Invalid key. Please enter an integer.")
