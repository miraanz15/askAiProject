import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

print("Asking the AI...")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": "How is AI evolving? Answer in five sentences"}
    ],
)

answer = response.choices[0].message.content

model = response.model

print(answer)
print(f"Answer from Model: {model}")



