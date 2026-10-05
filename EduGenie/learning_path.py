from gemini_client import generate_text


def generate_learning_path(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for a student who wants to learn:

{topic}

Organize the learning path from beginner to advanced.

Include:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Practice activities
5. Suggested learning resources

Use simple language and clear headings.
"""

    return generate_text(prompt)