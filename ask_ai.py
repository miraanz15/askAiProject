import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print(f"Key loaded. Starts with {api_key[:8]}, length {len(api_key)}.")
else:
    print("No key found. Check that .env exists and contains GROQ_API_KEY.")
