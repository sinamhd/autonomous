"""
File: langchain_openai_basic.py
Author: Sina Mehdinia
Date: 02/08/2025
Description: A basic example of using LangChain's ChatOpenAI integration to interact with OpenAI's API.

Usage:
1. Set up a .env file with your OpenAI API key.
2. Run the script with `python3 langchain_openai_basic.py`.
"""

import os

from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI


def main():
    """
    Main function to interact with OpenAI's ChatGPT via LangChain.

    - Loads environment variables from a .env file.
    - Initializes the OpenAI model with the specified parameters.
    - Sends a predefined user query and system message.
    - Prints the AI's response.
    """

    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found in the environment variables. Make sure to set it in your .env file."
        )

    # Initialize the OpenAI model via LangChain
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Define user query
    question = "What is the multiplication of 1248124 * 21421124?"

    # Set up conversation context
    messages = [
        ("system", "Respond short with emojis."),
        ("user", question),
    ]

    # Invoke the model and get the response
    response = model.invoke(messages)

    # Print the response
    print(f"AI Response: {response.content}")


if __name__ == "__main__":
    main()
