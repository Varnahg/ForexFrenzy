import os
from openai import OpenAI

import os
from openai import OpenAI


# Define the function
def get_answer(model, system_message, user_question):
    """
    Function to get an AI-generated response using the OpenAI API.

    Parameters:
    - model (str): The model to be used (e.g., "gpt-4").
    - system_message (str): The system's role message (e.g., "You are a helpful assistant").
    - user_question (str): The user's question to the AI.

    Returns:
    - str: The content of the AI's response.
    """
    # Retrieve the API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    # Check if the API key is found
    if not api_key:
        raise ValueError("API key not found. Make sure the 'OPENAI_API_KEY' environment variable is set.")

    # Initialize the OpenAI client with the retrieved API key
    client = OpenAI(api_key=api_key)

    # Create a chat completion request
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_question},
            ]
        )
        # Access the content of the response
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
if __name__ == "__main__":
    model = "gpt-4o"
    system_message = "You are a helpful assistant."
    user_question = "Search most recent news about the stock market."

    response = get_answer(model, system_message, user_question)
    print(response)


