import google.generativeai as genai
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from config folder
config_path = Path(__file__).parent.parent / "config" / ".env"
load_dotenv(config_path)

# Get API key with error handling
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-flash")


def analyze_gaps(resume_text, job_text):
    prompt = f"""
Compare the following resume with the job description and list key gaps or missing skills.

--- Job Description ---
{job_text}

--- Resume ---
{resume_text}

Only list missing skills or experience clearly.
"""
    return model.generate_content(prompt).text


def suggest_resume_tailoring(resume_text, job_text):
    prompt = f"""
You are a resume coach. Given the resume and job description, suggest how to rewrite or adjust the resume to fit the job better.

--- Job Description ---
{job_text}

--- Resume ---
{resume_text}

Give specific, actionable tailoring suggestions.
"""
    return model.generate_content(prompt).text


def generate_match_explanation(resume_text, job_text):
    prompt = f"""
Explain in friendly terms how well this resume fits the job description. Be short, clear, and helpful.

--- Job Description ---
{job_text}

--- Resume ---
{resume_text}
"""
    return model.generate_content(prompt).text
