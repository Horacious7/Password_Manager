# Password Manager Python

## Description
This is a simple password manager application created in Python using PyQt5 for the graphical interface and cryptography for security.
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Horacious7/Password_Manager.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Use the application's interface to add, view, or delete passwords.

## Features
- Add new passwords and their associated accounts.
- View stored passwords (decrypted).
- Delete passwords from the list.
- Data encryption to ensure security.

## Important Warning
**Please be careful when modifying or deleting the `passwords.pkl` or `secret.key` files.** If these files are corrupted or manually edited, the application might not work correctly. To fix any issues, delete these files and restart the application. The application will regenerate the necessary files upon restart.

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
