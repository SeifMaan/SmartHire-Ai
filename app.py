import streamlit as st
from resume_parser import extract_resume_data
from job_parser import extract_job_data
from matchmaker import match_resume_with_job
from gemini_helper import (
    analyze_gaps,
    suggest_resume_tailoring,
    generate_match_explanation,
)

st.set_page_config(page_title="SmartHire Resume Matcher", layout="centered")
st.title("🤖 SmartHire Resume Matcher Demo")

st.markdown(
    "Upload your **resume** and provide a **job listing URL** to see how well they match."
)

resume_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
job_url = st.text_input("🔗 Enter Job Listing URL (LinkedIn or other)")

if st.button("🔍 Match Resume with Job"):
    if resume_file and job_url:
        with open("uploaded_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        resume_data = extract_resume_data("uploaded_resume.pdf")
        job_data = extract_job_data(job_url)
        match_score = match_resume_with_job(resume_data, job_data)

        st.success(f"🎯 Match Score: **{round(match_score * 100, 2)}%**")

        # Save data for use by other buttons
        st.session_state.resume_data = resume_data
        st.session_state.job_data = job_data
    else:
        st.warning("⚠️ Please upload a resume and enter a job listing URL.")

if "resume_data" in st.session_state and "job_data" in st.session_state:
    st.markdown("## 💡 AI-Powered Suggestions")

    if st.button("🔍 Analyze Gaps"):
        response = analyze_gaps(
            st.session_state.resume_data["text"], st.session_state.job_data["text"]
        )
        st.markdown("### 🕳️ Gap Analysis")
        st.markdown(
            f"""
            <div style="padding: 1rem 0;">
                <pre style="white-space: pre-wrap; font-size: 16px; font-family: sans-serif;">{response}</pre>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button("🎯 Suggest Tailoring"):
        response = suggest_resume_tailoring(
            st.session_state.resume_data["text"], st.session_state.job_data["text"]
        )
        st.markdown("### ✂️ Resume Tailoring Suggestions")
        st.markdown(
            f"""
            <div style="padding: 1rem 0;">
                <pre style="white-space: pre-wrap; font-size: 16px; font-family: sans-serif;">{response}</pre>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.button("📖 Match Explanation"):
        response = generate_match_explanation(
            st.session_state.resume_data["text"], st.session_state.job_data["text"]
        )
        st.markdown("### 🧠 Match Explanation")
        st.markdown(
            f"""
            <div style="padding: 1rem 0;">
                <pre style="white-space: pre-wrap; font-size: 16px; font-family: sans-serif;">{response}</pre>
            </div>
            """,
            unsafe_allow_html=True,
        )
