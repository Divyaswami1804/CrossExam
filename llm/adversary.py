import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Read API key safely
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_counter(answer):
    try:
        prompt = f"""
You are a skeptical interviewer.
Do NOT be polite.
Point out logical flaws, exaggeration, and missing evidence.
Never praise the candidate.

Candidate answer:
{answer}

Respond in exactly 3 bullet points.
"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini error: {str(e)}"

