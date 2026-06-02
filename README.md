# 🎥 YouTube Summarizer

An AI-powered YouTube Summarizer built using **LangChain**, **Google Gemini**, and **Streamlit**. The application extracts transcripts from YouTube videos and converts them into structured, professional article-style summaries. It is designed to help users quickly understand the key insights from long-form video content without watching the entire video.

---

## 🚀 Project Overview

Watching lengthy YouTube videos to gather information can be time-consuming. This project automates the process by extracting the video transcript and leveraging Google's Gemini Large Language Model (LLM) to generate concise and well-structured articles.

The application intelligently handles both short and long videos. For long transcripts, it applies chunking and recursive summarization techniques to ensure efficient processing while preserving important information.

---

## ✨ Features

- Extracts transcripts from YouTube videos
- Generates professional article-style summaries
- Handles both short and long video content
- Recursive summarization for lengthy transcripts
- Dynamic workflow routing using LangChain RunnableBranch
- Streamlit-based user interface
- Gemini-powered content generation
- Organized output with headings and bullet points

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- YouTube Transcript API
- Recursive Character Text Splitter

---

## 🔄 Application Workflow

1. User enters a YouTube video URL.
2. Transcript is extracted from the video.
3. The application checks transcript length.
4. Short transcripts are summarized directly.
5. Long transcripts are split into smaller chunks.
6. Recursive summarization is applied to process large content efficiently.
7. Gemini generates a structured article.
8. The final article is displayed through the Streamlit interface.

---

## 📂 Project Structure

```text
youtube-summarizer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## 🧠 Key Concepts Implemented

- Prompt Engineering
- LangChain Pipelines
- RunnableLambda
- RunnableBranch
- Recursive Summarization
- Text Chunking
- LLM-Based Content Generation
- Streamlit Deployment

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/youtube-summarizer.git
cd youtube-summarizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```
## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Generative AI Applications
- LangChain Framework
- Large Language Model Integration
- Prompt Engineering
- Recursive Summarization
- Streamlit Application Development
- End-to-End AI Project Deployment



If you found this project useful, consider giving it a ⭐ on GitHub.
