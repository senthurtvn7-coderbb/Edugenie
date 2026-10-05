import time

from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL


if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str) -> str:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            return response.text or ""

        except Exception as e:
            error_text = str(e)

            if "503" in error_text and attempt < 2:
                wait_time = 5 * (attempt + 1)
                print(f"Gemini busy. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            raise
