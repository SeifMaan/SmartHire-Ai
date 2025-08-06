from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_with_job(resume_data, job_data):
    """
    Computes a similarity score between resume text and job description text using TF-IDF and cosine similarity.

    Args:
        resume_data (dict): Parsed resume data with key "text"
        job_data (dict): Parsed job data with key "text"

    Returns:
        float: Similarity score between 0.0 and 1.0
    """
    resume_text = resume_data.get("text", "")
    job_text = job_data.get("text", "")

    if not resume_text.strip() or not job_text.strip():
        return 0.0

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform([resume_text, job_text])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity)
    except Exception as e:
        print(f"[ERROR] Failed to calculate similarity: {e}")
        return 0.0
