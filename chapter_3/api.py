"""
File: api.py
Author: Sina Mehdinia
Date: 02/27/2025
Description: Implements a FastAPI-based backend to process receipt image uploads.
It extracts structured receipt data using the `process_receipt_bytes` function.

Usage:
1. Run the script with `uvicorn receipt_api:app --reload --port 1234`.
2. Open `http://localhost:1234/static/index.html` in your browser.
3. Upload a receipt image via the `/upload_receipt` endpoint.
"""

from fastapi import FastAPI, UploadFile, File
from receipt_processor import process_receipt_bytes
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Initialize the FastAPI app
app = FastAPI()

# Mount the static directory to serve frontend files (e.g., HTML, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    """
    Serves the frontend application.

    Returns:
    - FileResponse: Serves the `index.html` file from the `static` directory.
    """
    return FileResponse("static/index.html")


@app.post("/upload_receipt")
async def upload_receipt(file: UploadFile = File(...)):
    """
    Endpoint for uploading a receipt image.

    Steps:
    1. Reads the uploaded image file content into memory.
    2. Processes the receipt using `process_receipt_bytes`.
    3. Returns structured receipt data as JSON.

    Parameters:
    - file (UploadFile): The uploaded receipt image.

    Returns:
    - dict: JSON containing structured receipt details or an error message.
    """
    try:
        # Read the file content into memory
        file_content = await file.read()

        # Process the receipt image and extract structured data
        result = process_receipt_bytes(file_content)

    except Exception as e:
        # Handle errors and return an appropriate response
        return {"error": str(e)}

    return result
