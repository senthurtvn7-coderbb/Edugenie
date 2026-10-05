from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following text for a student.

Text:
{text}

Requirements:
- Keep the important points.
- Use simple language.
- Use headings and bullet points where helpful.
- Do not change the main meaning.
- Keep the summary concise but useful for studying.
"""

    return generate_text(prompt)