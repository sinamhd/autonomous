"""
File: langchain_gemini_tools.py
Author: Sina Mehdinia
Date: 02/08/2025
Description: Demonstrates using LangChain's tool system to perform function calling
with a custom Python function and Gemini's API.

Usage:
1. Set up a .env file with your Gemini API key.
2. Run the script with `python3 langchain_gemini_tools.py`.
"""

import os

from dotenv import find_dotenv, load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


def main():
    """
    Main function to demonstrate using LangChain's tool system
    with a custom Python function and Gemini's API.

    Steps:
    1. Load environment variables.
    2. Initialize Gemini model via LangChain.
    3. Bind tools to the model.
    4. Send a user query and handle tool calls.
    """

    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Get the API key from environment variables
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in the environment variables. Make sure to set it in your .env file."
        )

    # Initialize the Gemini model via LangChain
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

    # Register the custom function as a langchain tool
    @tool
    def multiply(a: int, b: int) -> int:
        """Multiplies a and b."""
        return a * b

    # Define tools (functions) for the model to use
    tools = [multiply]

    # Bind the tools to the model
    model_with_tools = model.bind_tools(tools)

    # Define the user question
    question = "What is the multiplication of 1248124 * 21421124?"

    # Set up conversation context (LangChain format)
    messages = [
        ("system", "Respond short with emojis."),
        ("user", question),
    ]

    # Call the model with tools enabled
    response_message = model_with_tools.invoke(messages)

    # Check if the model's response includes a tool call
    if response_message.tool_calls:
        # Append model's response to the conversation history
        messages.append(response_message)

        for tool_call in response_message.tool_calls:
            tool_name = tool_call["name"]

            # Check if the requested tool exists
            if tool_name == "multiply":
                # Execute the multiply function using LangChain's native tool execution
                tool_result = multiply.invoke(tool_call)

                # Append the tool response to the message history
                messages.append(tool_result)

        # Get a new response from the model after the function result is provided
        final_response = model_with_tools.invoke(messages)
        print(f"AI Response: {final_response.content}")

    else:
        # If no tool was identified, print the initial response
        print(f"AI Response: {response_message.content}")


if __name__ == "__main__":
    main()
