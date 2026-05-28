import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_MESSAGE = "You are a concise writing assistant."
PROMPT = "Explain what tokens are in large language models using a simple analogy."
MAX_TOKENS = 120
TEMPERATURES = [0.0, 0.7, 1.2]


def ask_with_temperature(temperature):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": PROMPT},
        ],
        temperature=temperature,
        max_tokens=MAX_TOKENS,
    )

    return response.choices[0].message.content


def main():
    print(f"Prompt: {PROMPT}\n")

    for temperature in TEMPERATURES:
        print(f"--- Temperature: {temperature} ---")
        print(ask_with_temperature(temperature))
        print()


if __name__ == "__main__":
    main()
