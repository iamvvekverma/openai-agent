# OpenAI Python API Starter

This project shows how to call an OpenAI model directly from Python instead of using ChatGPT in the browser. It uses the current OpenAI Python client style:

```python
from openai import OpenAI

client = OpenAI()
```

The goal is to understand the foundation of LLM programming: loading an API key from an environment variable, sending a chat request, changing the system message, limiting output with `max_tokens`, and comparing how `temperature` affects model responses.

## What This Project Contains

- `main.py` - asks for user input and returns one model response.
- `compare_temperatures.py` - sends the same prompt at different temperature values so you can compare the output.
- `.env.example` - shows where the API key goes without committing a real key.
- `explanation/code_explanation.md` - explains the code line by line and describes the main API concepts.

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- `openai >= 1.0.0`
- `python-dotenv`

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create your local `.env` file from the example:

```bash
cp .env.example .env
```

3. Put your API key inside `.env`:

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
```

Leave `OPENAI_API_KEY` blank until you have your own key. The `.env` file is ignored by Git so your real key does not get uploaded to GitHub.

## Run the User Input Script

```bash
python main.py
```

Type a question when prompted. The script sends your input to the model and prints the response.

## Compare Temperatures

```bash
python compare_temperatures.py
```

This sends the same prompt three times with different temperature values:

- `0.0` for focused and predictable output
- `0.7` for balanced output
- `1.2` for more varied and creative output

## Important Note

This project uses `client.chat.completions.create()` because that is the API method required for this assignment. OpenAI also has newer APIs for some use cases, but this project intentionally stays simple and focused on Chat Completions.
