"""
File: openai_basic_call.py
Author: Sina Mehdinia
Date: 01/24/2025
Description: A basic example of using OpenAI's Chat Completion API to answer a question.

Usage:
1. Set up a .env file with your OpenAI API key.
2. Run the script with `python3 openai_basic_call.py`.
"""

import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv(find_dotenv())

# Initialize the OpenAI client with the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Specify the model to use
model = "gpt-4o-mini"

# Define the user's question
question = "What is the multiplication of 1248124 * 21421124"


# Create a conversation context for the AI
messages = [
    {
        "role": "system",
        "content": "Respond short with emojis.",
    },  # System instruction for the AI
    {"role": "user", "content": question},  # User-provided input
]


# Call the OpenAI Chat Completion API
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,  # Temperature controls randomness; 0 for more predictable output
)

# Extract and display the AI's response
response_message = response.choices[0].message.content
print(response_message)
