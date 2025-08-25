# 🧠 CrewAI SEO Analysis Agent  
Internship Submission for CrowdWisdomTrading

This project is a Python-based SEO analysis tool powered by CrewAI and LiteLLM. It was developed for the internship assessment from CrowdWisdomTrading. The solution uses multiple AI agents to extract, analyze, and report SEO insights from any webpage URL. It includes both a command-line interface (CLI) and a web-based user interface built with Flask.

---

## 📌 Project Overview

✅ Web scraping and content extraction from any given URL  
✅ SEO evaluation: keyword analysis, structure, meta tags, internal linking  
✅ Final recommendation report in natural language  
✅ Web interface (Flask) for user-friendly input/output  
✅ Built using CrewAI agent framework with LiteLLM + custom model

---

## 🛠️ Tech Stack

- Python 3.10+
- CrewAI
- LiteLLM
-  OpenRouter LLM API
- Flask (for web interface)

---

## 👥 Agent Flow (CrewAI)

| Agent Role         | Description |
|--------------------|-------------|
| SEO Research Agent | Scrapes and summarizes text from the URL |
| SEO Analysis Agent | Analyzes structure, headings, keywords, etc. |
| SEO Report Agent   | Generates final SEO recommendations report |

All agents run in a sequential CrewAI flow with guardrails.

---

## 🔄 Input/Output Example

### 🧾 Sample Input

URL:
https://brightdata.com/blog/ai/geo-and-seo-ai-agent
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d824b636-ba71-438b-b09c-6d53184bbfa7" />


### 📊 Sample Output

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/86dea4d5-88ce-4a3b-a6a5-1e67f5870f67" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/60f5b200-493a-4f79-84d9-fa2f5b0674f5" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/31e65d58-2e95-4858-9782-445575ad93bd" />




---

## ▶️ How to Run the Project

### 1. Clone the Repository
### 2. Install Requirements (crewai , litellm , flask)
### 3. Set LLM API Key (Hugging Face or OpenRouter)
### 4. Run The Project

## 📁 Project Structure

SEO-analyzer/
├── app.py                       # Main Flask app that includes CrewAI SEO logic
├── requirements.txt            # All Python dependencies
├── README.md                   # Project documentation
│
├── static/
│   └── style.css               # CSS styling for the Flask frontend
│
├── templates/
│   ├── index.html              # HTML form to submit a URL
│   └── report.html             # HTML page to display the SEO report
│
└── output_examples/
    └── sample_output.md       # Example output from the SEO agent (optional)
