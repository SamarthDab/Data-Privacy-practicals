'''Write a program that generates a password using a random combination of 
words from a dictionary file.'''


import random

def generate_password(dict_file, num_words, separator):
    """
    Args:
        dict_file (str): Path to the dictionary file (one word per line).
        num_words (int): Number of words to combine.
        separator (str): String to separate the words.
    Returns:
        str: Generated password.
    """

    with open(dict_file, 'r') as f:
        words = [line.strip() for line in f if line.strip()]
    
    if len(words) < num_words:
        raise ValueError("Dictionary file does not have enough words.")
    
    chosen_words = random.sample(words, num_words)
    password = separator.join(chosen_words)
    return password

if __name__ == '__main__':
    dict_path = input("Enter the path to dictionary file: ")
    num_words = int(input("Enter how many words in the password: "))
    separator = input("Enter the separator (e.g., '-', '', '_'): ")
    
    password = generate_password(dict_path, num_words, separator)
    print(f"Generated password: {password}")