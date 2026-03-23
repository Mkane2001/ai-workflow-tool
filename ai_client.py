import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(prompt: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"DEMO_MODE::{str(e)}"