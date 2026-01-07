import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = '''
You are a clinic FAQ assistant.
Answer ONLY using the provided context.
If the answer is not present, say:
"I don’t have that information."
'''

def generate_answer(question: str, context: list[str]):
    joined_context = "\n".join(context)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{joined_context}\n\nQuestion:\n{question}"}
        ]
    )

    return response.choices[0].message.content
