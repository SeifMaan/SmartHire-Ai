from PyPDF2 import PdfReader
import pdfplumber  

def extract_resume_data(pdf_path, max_chars=3000):
    text = ""
    
    try:
        # Try using PyPDF2 first
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        
        # Fallback to pdfplumber if PyPDF2 fails or returns blank
        if not text.strip():
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
                    
        if not text.strip():
            return {"text": "⚠️ Could not extract any readable text from the PDF."}

        return {"text": text[:max_chars]}
    
    except Exception as e:
        return {"text": f"❌ Error reading resume: {e}"}
