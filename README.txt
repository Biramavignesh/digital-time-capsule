DIGITAL TIME CAPSULE PROJECT
Project Description

The Digital Time Capsule is a Python-based security application that allows users to store messages that are locked until a specific future date. It uses AES-256 encryption via the Fernet system to ensure that the message cannot be read by simply opening the storage file; the data is only decrypted when the system clock reaches or exceeds the user-defined unlock date.
Features

    Secure message encryption using the cryptography library.

    Automatic key generation and management.

    Metadata storage in JSON format.

    Time-lock validation to prevent early access.

    Easy-to-use Command Line Interface (CLI).

Prerequisites

To run this project, you must have Python 3.x installed and the cryptography library. You can install the required library using:
pip install cryptography
Files Included

    time_capsule.py: The main source code containing the encryption and logic.

    README.txt: Documentation and instructions (this file).

    requirements.txt: List of dependencies.

How to Run

    Open your terminal or command prompt.

    Navigate to the project directory.

    Run the script: python time_capsule.py

    To Create: Type seal, enter your secret message, and provide a date in YYYY-MM-DD format.

    To Open: Run the script again and type open. The script will check the date and reveal the message only if the time has passed.

Technical Implementation Details

    Encryption: The project utilizes the Fernet (symmetric encryption) implementation which guarantees that a message encrypted with it cannot be manipulated or read without the key.

    Storage: Data is serialized into a JSON object, making it lightweight and portable.

    Security Note: The capsule.key file is required for decryption. If this file is lost, the capsule cannot be recovered.

Author

S.Biramavignesh
Registration Number:25BEC10029
Date: April 1, 2026