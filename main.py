import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_MESSAGE = "You are a helpful assistant who explains things clearly and simply."
TEMPERATURE = 0.7
MAX_TOKENS = 150


def get_model_response(user_prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_prompt},
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    return response.choices[0].message.content


def main():
    user_prompt = input("Ask the model something: ")

    if not user_prompt.strip():
        print("Please enter a question or prompt.")
        return

    answer = get_model_response(user_prompt)
    print("\nModel response:\n")
    print(answer)


if __name__ == "__main__":
    main()
