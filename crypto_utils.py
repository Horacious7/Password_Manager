import sys
import os
sys.path.append(r"C:\Users\maier\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from cryptography.fernet import Fernet

def generate_key(key_file="secret.key"):
    """Generate a key and save it into a file."""
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)

def load_key(key_file="secret.key"):
    """Load the previously generated key."""
    if not os.path.exists(key_file):
        generate_key(key_file)
    return open(key_file, "rb").read()

def encrypt_message(key, message):
    """Encrypts a message."""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    """Decrypts an encrypted message."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message
