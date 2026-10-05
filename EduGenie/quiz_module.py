from gemini_client import generate_text


def generate_quiz(topic: str) -> str:
    prompt = f"""
Create a quiz for a student about this topic:

{topic}

Requirements:
- Create exactly 3 multiple-choice questions.
- Each question must have exactly 4 options.
- Clearly show the correct answer.
- Add a short explanation for each answer.
- Keep the questions suitable for students.
- Use simple, clear language.

Format:

## Question 1
A. Option
B. Option
C. Option
D. Option

Answer: B
Explanation: ...

## Question 2
...

## Question 3
...
"""

    return generate_text(prompt)