import os
import openai
from dotenv import load_dotenv
a
# Load environment variables from .env file
load_dotenv()

# Get API key from environment varhiable
api_key = os.getenv("api_key")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)


def chat_bot(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_bot(user_input)
        print("Chatbot:", response)
