from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.
Use simple language that a student can understand.

Student question:
{question}

Give a helpful answer with headings or bullet points when useful.
"""

    return generate_text(prompt)