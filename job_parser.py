import requests
from bs4 import BeautifulSoup


def extract_job_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # raise error for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        # Try more intelligent ways to extract job content
        job_text = []

        # Try LinkedIn-specific div (optional)
        main_content = soup.find("div", {"class": "show-more-less-html__markup"})
        if main_content:
            job_text.append(main_content.get_text(separator=" ", strip=True))

        # Fallback: use <p> tags
        if not job_text:
            paragraphs = soup.find_all("p")
            job_text = [p.get_text(strip=True) for p in paragraphs]

        text = " ".join(job_text)
        return (
            {"text": text[:3000]} if text else {"text": "⚠️ No job description found."}
        )

    except requests.exceptions.RequestException as req_err:
        return {"text": f"❌ Network error: {req_err}"}
    except Exception as e:
        return {"text": f"❌ Error extracting job: {e}"}
