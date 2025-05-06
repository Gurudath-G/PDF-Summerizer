#AI-powered PDF Summarizer

**AI-powered PDF Summarizer** is a cutting-edge PDF summarization tool that leverages state-of-the-art AI models to extract and synthesize information from PDF documents. Built with Meta's LLaMA 4 MOE Maverick model and powered by Groq's inference engine, it provides blazing-fast, high-precision summaries for any PDF document.

---

## Features

- **Intelligent PDF Processing**: Convert PDFs to images and extract detailed information
- **Advanced Summarization**: Generate comprehensive, well-structured summaries using LLaMA 4 MOE Maverick
- **Professional PDF Export**: Download summaries as beautifully formatted PDF documents
- **Modern Web Interface**: Clean, responsive UI built with Streamlit
- **Parallel Processing**: Multi-threaded extraction for improved performance
- **Docker Support**: Easy deployment with containerization
- **CI/CD Integration**: Automated Docker image builds and pushes

---

## Table of Contents

1. [Architecture](#architecture)
2. [Technical Stack](#technical-stack)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Docker Deployment](#docker-deployment)
7. [Project Structure](#project-structure)
8. [Screenshots](#screenshots)

---

## Architecture

AI-powered PDF Summarizer follows a pipeline architecture with three main components:

1. **PDF Processing**: Converts PDF documents to images for processing
2. **Detail Extraction**: Uses LLaMA 4 MOE Maverick to extract detailed information from each page
3. **Summary Generation**: Synthesizes extracted information into a coherent, analytical summary

The pipeline is optimized for parallel processing and handles documents of varying lengths efficiently.

---

## Technical Stack

- **Language**: Python 3.10
- **Web Framework**: Streamlit
- **AI Models**: Meta's LLaMA 4 MOE Maverick
- **Inference Engine**: Groq
- **PDF Processing**: pdf2image, ReportLab
- **Package Management**: uv
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

---

## Requirements

- Python 3.10 or higher
- Dependencies listed in `pyproject.toml`
- `.env` file containing Groq API key
- Poppler utils for PDF processing

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AlphaExtract.git
   cd AlphaExtract
Install dependencies using uv:

bash
Copy
Edit
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
Create a .env file in the root directory and add your Groq API key:

ini
Copy
Edit
GROQ_API_KEY=your_actual_groq_api_key
Run the application:

bash
Copy
Edit
streamlit run main.py
How the API Key is Loaded
In the code, the following snippet loads your .env file securely:

python
Copy
Edit
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
Make sure .env is in the root directory and not checked into version control (add it to .gitignore).

Usage
Access the web interface at http://localhost:7860

Upload your PDF document using the sidebar

Wait for the processing to complete

View the generated summary

Download the summary as a PDF document

Docker Deployment
Build the Docker image:

bash
Copy
Edit
docker build -t alphaextract .
Run the container:

bash
Copy
Edit
docker run -p 7860:7860 --env-file .env alphaextract
The application will be available at http://localhost:7860.

Project Structure
css
Copy
Edit
AlphaExtract/
├── .github/
│   └── workflows/
│       └── dockerhubPush.yaml
├── src/
│   ├── components/
│   │   ├── extractPdfDetails.py
│   │   └── summaryEngine.py
│   ├── pipelines/
│   │   └── pipeline.py
│   └── utils/
│       ├── functions.py
│       └── logger.py
├── config.ini
├── Dockerfile
├── main.py
├── prompts.yaml
├── .env
└── pyproject.toml
Screenshots
Project Demo

Complete demonstration of PDF upload, processing, and summary generation

Application Interface

The clean and intuitive application interface

License
This project is licensed under the MIT License.

Author
Created with ❤️ by Rauhan Ahmed Siddiqui.

For questions or support, please open an issue on the GitHub repository.

yaml
Copy
Edit

---

Would you like me to save this as a file and return the download link?






