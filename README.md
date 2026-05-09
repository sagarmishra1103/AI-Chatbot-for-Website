
# AI Chatbot for Website

A modular system designed to extract and clean website content, retrieve relevant information for user queries, and generate context-grounded answers using the Google Gemini API. This project focuses on accuracy by strictly limiting responses to the scraped content, effectively reducing AI hallucinations. [cite: 428, 429]

## 🚀 Features
* **Structured Web Scraping**: Uses `Requests` and `BeautifulSoup` to extract meaningful content while stripping noise like scripts and navbars. [cite: 431, 582]
* **Context-Grounded Answers**: Engineered to answer questions using only the content extracted from user-provided URLs. [cite: 437, 441]
* **Efficient Retrieval**: Implements a lightweight, keyword-based ranking system for fast and cost-efficient information retrieval. [cite: 558, 559]
* **Session Caching**: Uses intelligent caching to store scraped chunks, allowing for faster response times in the same session. [cite: 447, 460]
* **Interactive UI**: Built with Streamlit for a clean, user-friendly experience. [cite: 430, 647]

## 🏗️ Architecture & Data Flow
The system follows a structured multi-stage pipeline: [cite: 450]
1. **URL Input**: User provides a website link. [cite: 438, 452]
2. **Scraping & Cleaning**: Raw HTML is extracted and converted into structured text. [cite: 443, 444, 453, 454]
3. **Chunking**: Content is segmented into LLM-friendly chunks with overlapping segments to prevent context loss. [cite: 491, 492]
4. **Retrieval**: The most relevant chunks are ranked and selected based on the user's query. [cite: 445, 459]
5. **Prompt Synthesis**: A context-aware prompt is built using the retrieved chunks and chat history. [cite: 539, 545]
6. **Gemini Response**: The Google Gemini API generates a precise answer. [cite: 520, 532]

## 📁 Repository Structure
```text
Chatbot/
├── components/
│   ├── context_builder.py       # Text cleaning & chunking
│   ├── gemini_client.py         # Gemini API integration
│   ├── prompt_engine.py         # Prompt construction logic
│   ├── retriever.py             # Keyword-based ranking
│   └── url_mode_web_scrap.py    # Web scraping module
├── utils/
│   └── logger.py                # Logging utility
├── app.py                       # Main Streamlit application
├── .env                         # Configuration for API keys
└── requirements.txt             # Project dependencies
```
  🛠️ Installation & Setup
  1. Clone the Repository
  ```Bash
git clone [https://github.com/sagarmishra1103/AI-Chatbot-for-Website.git](https://github.com/sagarmishra1103/AI-Chatbot-for-Website.git)
cd AI-Chatbot-for-Website
  ```
  2. Set Up Virtual Environment <br>

For Windows (PowerShell):

```PowerShell
   python -m venv .venv
   .venv\\Scripts\\Activate.ps1
   pip install -r requirements.txt
```

For MacOS/Linux (Bash):
```Bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

  4. Configuration
Create a .env file in the project root and add your Google Gemini API key:
```Code snippet
GEMINI_API_KEY="YOUR_KEY_HERE"
```
  💻 Running the ApplicationLaunch the chatbot using the following command:
  ```Bash
streamlit run app.py
```
  Once running, the interface will be available at `http://localhost:8501.`   
  📦 Dependencies
  - Streamlit
  - Requests
  - BeautifulSoup
  - Google Generative AI SDK
  - python-dotenv
  
---
Author: Shivsagar Mishra 

