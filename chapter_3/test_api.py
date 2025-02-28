"""
File: test_api.py
Author: Sina Mehdinia
Date: 02/27/2025
Description: Tests the FastAPI receipt processing endpoint by uploading an image file.

Usage:
1. Ensure the FastAPI server is running (from api.py).
2. Update `file_path` to point to a valid receipt image.
3. Run the script with `python3 test_api.py`.
"""

import requests

# Define the FastAPI endpoint URL (ensure the server is running)
url = "http://localhost:1234/upload_receipt"

# Path to the test receipt image (update with an actual file path)
file_path = "../your_sample_receipt.jpg"

# Open and send the file as part of the HTTP POST request
with open(file_path, "rb") as file:
    files = {"file": (file_path, file, "image/jpeg")}
    
    # Send the request and capture the response
    response = requests.post(url, files=files)

# Print the JSON response from the server
print(response.json())
