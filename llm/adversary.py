import google.generativeai as genai

genai.configure(api_key="AIzaSyAvmvx_hH_cbvBvSK0EDurj6JiIr0sYg2M")

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

