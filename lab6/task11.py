import string

def generate_text_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}")

generate_text_files()
