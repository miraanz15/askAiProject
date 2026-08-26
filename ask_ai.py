import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

print("Ask me anything. Type 'quit' to stop.")

while True:
    question = input("\nYour question: ")

    if question.strip().lower() == "quit":
        print("Goodbye!")
        break

    if not question.strip():
        print("Please type something.")
        continue

    print("\nAsking the AI...")

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": question}
        ],
    )

    answer = response.choices[0].message.content

    print(f"\nAnswer is: {answer}")
