import pickle
import os
from crypto_utils import load_key, encrypt_message, decrypt_message

class PasswordManager:
    def __init__(self, key_file="secret.key", password_file="passwords.pkl"):
        self.key_file = key_file
        self.password_file = password_file
        self.key = load_key(self.key_file)
        self.passwords = self.load_passwords()

    def save_passwords(self):
        """Save the passwords to a file."""
        with open(self.password_file, "wb") as f:
            pickle.dump(self.passwords, f)

    def load_passwords(self):
        """Load passwords from a file."""
        if os.path.exists(self.password_file):
            with open(self.password_file, "rb") as f:
                return pickle.load(f)
        return []

    def add_password(self, account, password):
        """Add an encrypted password to the list."""
        encrypted_password = encrypt_message(self.key, password)
        self.passwords.append((account, encrypted_password))
        self.save_passwords()

    def view_passwords(self):
        """View all decrypted passwords."""
        return [(account, decrypt_message(self.key, encrypted_password)) for account, encrypted_password in self.passwords]

    def delete_password(self, account):
        """Delete a password by account name."""
        self.passwords = [entry for entry in self.passwords if entry[0] != account]
        self.save_passwords()
