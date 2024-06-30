import openai 
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

try:
    response = client.completions.create(model="gpt-3.5-turbo",
    prompt="Hello, how are you?",
    max_tokens=5)
    print(response.choices[0].text.strip())
except openai.RateLimitError:
    print("RateLimitError: You have exceeded your rate limit.")
except Exception as e:
    print(f"An error occurred: {e}")
