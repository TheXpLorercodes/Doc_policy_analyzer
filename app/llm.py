from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_answer(context, question):

    gemini_api_key = os.getenv("AIzaSyD2QyTxnIKm1Hrb0HGthZdfK8ULlT0xuG4")

    client = genai.Client(api_key=gemini_api_key)

    system_prompt = f"""
You are an HR assistant.

Use ONLY the information provided in the context.

Rules:
1. Do not add information not present in the context
2. Ignore irrelevant parts
3. If answer is missing say:
"This question is outside the provided documents."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt
    )

    return response.text