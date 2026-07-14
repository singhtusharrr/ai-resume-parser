import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume_text):

    prompt = f"""
You are an expert HR Recruiter.

Analyze this resume and return ONLY in this format:

Name:
Email:
Phone:
Skills:
Education:
Experience:
Projects:
ATS Score:
Suggestions:

Resume:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text