from cryptography.fernet import Fernet
from django.conf import settings
import base64
import os

# Load fixed secret key
KEY_FILE = os.path.join(os.path.dirname(__file__), 'secret.key')

with open(KEY_FILE, 'rb') as f:
    raw_key = f.read()

# Fernet needs 32-byte base64 key
key = base64.urlsafe_b64encode(raw_key.ljust(32, b'0'))
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()
