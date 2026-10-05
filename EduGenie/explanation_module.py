from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the following topic as an educational tutor.

Topic:
{topic}

Explain it in simple language.
Include:
1. Definition
2. Main points
3. Simple example
4. Short conclusion
"""

    return generate_text(prompt)