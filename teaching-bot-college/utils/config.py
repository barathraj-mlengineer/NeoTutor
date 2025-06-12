import os
from dotenv import load_dotenv

load_dotenv()

def load_api_key(key):
    return os.getenv(key)
