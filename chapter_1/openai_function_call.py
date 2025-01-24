"""
File: openai_function_call.py
Author: Sina Mehdinia
Date: 01/24/2025
Description: Demonstrates using OpenAI's function-calling feature with a custom Python function.

Usage:
1. Set up a .env file with your OpenAI API key.
2. Run the script with `python3 openai_function_call.py`.
"""

import json
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv(find_dotenv())

# Initialize the OpenAI client with the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Specify the model to use
model = "gpt-4o-mini"


# Define a custom function to multiply two integers
def multiply(parameters):
    number1 = parameters["number1"]
    number2 = parameters["number2"]
    return number1 * number2


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
question = "What is the multiplication of 1248124 * 21421124"

# Create the initial conversation context
messages = [
    {
        "role": "system",
        "content": "Respond short with emojis.",
    },  # System instruction for the model
    {"role": "user", "content": question},  # User's query
]

# Call the OpenAI Chat Completion API
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,  # Temperature controls randomness; 0 for more predictable output
    tools=tools,  # Tools the model can use
    tool_choice="auto",  # Let the model decide if a tool is required
)

# Extract the model's initial response
response_message = response.choices[0].message
# print('Initial response message:\n', response_message)

# Append the response to the conversation history
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
        results = multiply(tool_arguments)

        # Append the tool response to the message history
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": tool_function_name,
                "content": str(results),
            }
        )

        # Get a new response from the model after the function result is provided
        model_response_with_function_call = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        print(model_response_with_function_call.choices[0].message.content)
    else:
        # Handle invalid or unsupported function names
        print(f"Error: function {tool_function_name} does not exist")
else:
    # If no tool was identified, print the initial response
    print(response_message.content)
