from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smarthire-resume-matcher",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered resume matching tool using Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/smarthire-resume-matcher",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Human Resources",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "google-generativeai>=0.3.0",
        "python-dotenv>=1.0.0",
        "PyPDF2>=3.0.1",
        "pdfplumber>=0.9.0",
        "scikit-learn>=1.3.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
    ],
)
