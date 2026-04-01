import json
import datetime
import os
from cryptography.fernet import Fernet

def get_key():
    # Load existing key or create a new one
    if not os.path.exists("capsule.key"):
        key = Fernet.generate_key()
        with open("capsule.key", "wb") as key_file:
            key_file.write(key)
    return open("capsule.key", "rb").read()

def seal_capsule():
    message = input("Enter the message for the future: ")
    date_input = input("Enter unlock date (YYYY-MM-DD): ")
    
    # Encrypt the message
    key = get_key()
    f = Fernet(key)
    encrypted_bytes = f.encrypt(message.encode())
    
    # Package data
    capsule_content = {
        "unlock_date": date_input,
        "data": encrypted_bytes.decode()
    }
    
    with open("time_capsule.json", "w") as file:
        json.dump(capsule_content, file)
    
    print("Capsule stored. It will remain locked until " + date_input)

def open_capsule():
    if not os.path.exists("time_capsule.json"):
        print("No capsule found.")
        return

    with open("time_capsule.json", "r") as file:
        content = json.load(file)
    
    # Date comparison logic
    target_date = datetime.datetime.strptime(content["unlock_date"], "%Y-%m-%d")
    current_date = datetime.datetime.now()
    
    if current_date >= target_date:
        key = get_key()
        f = Fernet(key)
        decrypted_message = f.decrypt(content["data"].encode()).decode()
        print("Capsule Opened!")
        print("Message: " + decrypted_message)
    else:
        wait_time = target_date - current_date
        print("The capsule is still locked.")
        print("Time remaining: " + str(wait_time.days) + " days.")

# Simple CLI Interface
print("--- Digital Time Capsule ---")
action = input("Type 'seal' to create or 'open' to check: ").lower()

if action == "seal":
    seal_capsule()
elif action == "open":
    open_capsule()
else:
    print("Invalid command.")
