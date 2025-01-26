"""
File: openai_basic_call.py
Author: Sina Mehdinia
Date: 01/26/2025
Description: A basic example of using OpenAI's Chat Completion API to answer a question.

Usage:
1. Set up a .env file with your OpenAI API key.
2. Run the script with `python3 openai_basic_call.py`.
"""

import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

def main():
    """
    Main function to demonstrate how to interact with the OpenAI API.
    Learn how to:
    1. Set up and load environment variables.
    2. Initialize the OpenAI client.
    3. Send a question and receive a response from the AI.
    """
    # Load environment variables from .env file
    load_dotenv(find_dotenv())
    
    # Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in the environment variables. Make sure to set it in your .env file.")
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Specify the model and user input
    model = "gpt-4o-mini"
    question = "What is the multiplication of 1248124 * 21421124?"
    
    # Set up conversation context
    messages = [
        {"role": "system", "content": "Respond short with emojis."},
        {"role": "user", "content": question},
    ]
    
    # Call the API and get a response
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    
    # Print the response
    response_message = response.choices[0].message.content
    print(f"AI Response: {response_message}")

if __name__ == "__main__":
    main()