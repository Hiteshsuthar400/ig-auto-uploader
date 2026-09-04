import os
from dotenv import load_dotenv

# Load the user inputs from the .env file
load_dotenv()

# Assign them to variables
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

# Validation check
if not all([IG_USERNAME, IG_PASSWORD, GEMINI_API_KEY, DRIVE_FOLDER_ID]):
    raise ValueError("Missing credentials! Please check your .env file.")
