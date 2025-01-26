"""
File: openai_function_call.py
Author: Sina Mehdinia
Date: 01/26/2025
Description: Demonstrates using OpenAI's function-calling feature with a custom Python function.

Usage:
1. Set up a .env file with your OpenAI API key.
2. Run the script with `python3 openai_function_call.py`.
"""

import json
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI


def multiply(parameters):
    """
    Custom function to multiply two integers.

    Args:
        parameters (dict): A dictionary containing two integers, "number1" and "number2".

    Returns:
        int: The multiplication result of number1 and number2.
    """
    number1 = parameters["number1"]
    number2 = parameters["number2"]
    return number1 * number2


def main():
    """
    Main function to demonstrate using OpenAI's function-calling feature
    with a custom Python function.
    Learn how to:
    1. Load environment variables.
    2. Set up a custom function for the AI to use.
    3. Interact with OpenAI's function-calling feature to execute the function.
    """
    # Load environment variables from .env file
    load_dotenv(find_dotenv())
    
    # Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in the environment variables. Make sure to set it in your .env file.")
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Specify the model to use
    model = "gpt-4o-mini"
    
    # Define tools (functions) for the model to use
    tools = [
        {
            "type": "function",
            "function": {
                "name": "multiply",
                "description": "Use this function to multiply two integers and return the result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number1": {
                            "type": "integer",
                            "description": "The first integer to multiply.",
                        },
                        "number2": {
                            "type": "integer",
                            "description": "The second integer to multiply.",
                        },
                    },
                    "required": ["number1", "number2"],
                },
            },
        }
    ]
    
    # Define the user question
    question = "What is the multiplication of 1248124 * 21421124?"
    
    # Set up conversation context
    messages = [
        {
            "role": "system",
            "content": "Respond short with emojis.",
        },
        {"role": "user", "content": question},
    ]
    
    # Call the OpenAI Chat Completion API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        tools=tools,
        tool_choice="auto",  # Let the model decide if a tool is required
    )
    
    # Extract the model's initial response
    response_message = response.choices[0].message
    messages.append(response_message)
    
    # Check if the model's response includes a tool call
    tool_calls = response_message.tool_calls
    if tool_calls:
        # Extract details about the tool call
        tool_call_id = tool_calls[0].id
        tool_function_name = tool_calls[0].function.name
        tool_arguments = json.loads(tool_calls[0].function.arguments)
        
        if tool_function_name == "multiply":
            # Execute the multiply function
            result = multiply(tool_arguments)
            
            # Append the tool response to the message history
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call_id,
                    "name": tool_function_name,
                    "content": str(result),
                }
            )
            
            # Get a new response from the model after the function result is provided
            model_response_with_function_call = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            print(f"AI Response: {model_response_with_function_call.choices[0].message.content}")
        else:
            print(f"Error: function {tool_function_name} does not exist")
    else:
        # If no tool was identified, print the initial response
        print(f"AI Response: {response_message.content}")


if __name__ == "__main__":
    main()
