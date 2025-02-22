import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_input):
    """
    Generate a response from the GPT-4o model based on user input.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()
