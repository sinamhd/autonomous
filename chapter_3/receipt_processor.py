"""
File: receipt_processor.py
Author: Sina Mehdinia
Date: 02/27/2025
Description: Extracts structured receipt data from an image using
Google's Gemini 2.0 Flash model or OpenAI's GPT-4o-mini.

Usage:
1. Run the script with `python3 receipt_processor.py`.
2. Ensure that the sample image path is correct before running.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import find_dotenv, load_dotenv
import base64
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.messages import HumanMessage

# Load environment variables (Ensure a .env file exists with API keys)
load_dotenv(find_dotenv())


def encode_image(image_path: str) -> str:
    """
    Encodes an image file into a base64 string.

    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - str: Base64-encoded string representation of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Define Pydantic models to structure receipt data
class MerchantInfo(BaseModel):
    """Represents merchant information on a receipt."""
    name: str
    address: str


class Item(BaseModel):
    """Represents an item on a receipt."""
    name: str
    quantity: int
    price: float


class TransactionDetails(BaseModel):
    """Stores transaction details from a receipt."""
    date: str
    subtotal: float
    tax: float
    tip: Optional[float]
    discount: Optional[float]
    total: float


class Receipt(BaseModel):
    """Represents a structured receipt with merchant, transaction, and item details."""
    merchant: MerchantInfo
    transaction: TransactionDetails
    items: List[Item]


# Initialize language models (ensure correct API setup in .env)
#model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# Make the model generate structured outputs
model_structured = model.with_structured_output(Receipt)


def process_receipt_bytes(image_bytes: bytes) -> dict:
    """
    Processes a receipt image given as raw bytes.

    Steps:
    1. Encodes the image bytes into a base64 string.
    2. Creates a message with both text and image content.
    3. Uses Gemini to extract structured receipt data.

    Parameters:
    - image_bytes (bytes): Raw image bytes of the receipt.

    Returns:
    - dict: JSON-serializable dictionary with structured receipt data.
    """
    # Convert the image bytes to a base64-encoded string
    image_data = base64.b64encode(image_bytes).decode("utf-8")

    # Construct the message format for model invocation
    message = HumanMessage(
        content=[
            {"type": "text", "text": "Extract the transactions from the image."},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ],
    )

    # Call the structured model to extract receipt data
    receipt = model_structured.invoke([message])

    return receipt


# Sample execution for extracting receipt details from an image
if __name__ == "__main__":      
    # Define the path to the sample receipt image
    sample_image_path = "../your_sample_receipt.jpg"

    try:
        # Read the image as raw bytes
        with open(sample_image_path, "rb") as f:
            image_bytes = f.read()

        # Process the receipt image
        result = process_receipt_bytes(image_bytes)

        # Display extracted receipt data
        print("Extracted Receipt Data:")
        print(result)

    except Exception as e:
        # Handle errors in file reading or processing
        print(f"Error processing receipt: {e}")
