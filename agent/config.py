import os

LLM_PROVIDER = "openai"
OPENAI_MODEL = "gpt-4.1-mini"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Set it in the .env file.")
