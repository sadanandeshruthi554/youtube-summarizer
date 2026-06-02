import os
from dotenv import load_dotenv

from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

from langchain_text_splitters import RecursiveCharacterTextSplitter

# -----------------------------
# STEP 1: Load API Key
# -----------------------------
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# -----------------------------
# STEP 2: Initialize LLM
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3
)

# -----------------------------
# STEP 3: Extract Transcript
# -----------------------------
def extract_transcript(video_url):
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=False,
        language=["en"]
    )

    docs = loader.load()
    return docs[0].page_content
# -----------------------------
# STEP 4: Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_template("""
Convert transcript into a professional article.

Rules:
- Ignore intro like welcome, subscribe
- Focus on useful content
- Use headings and bullet points

Transcript:
{text}
""")

# -----------------------------
# STEP 5: Basic Summarizer (Short Videos)
# -----------------------------
base_summarizer = (
    prompt
    | llm
    | StrOutputParser()
)

# -----------------------------
# STEP 6: Chunking for Long Videos
# -----------------------------
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    return splitter.split_text(text)

# -----------------------------
# STEP 7: Recursive Summarization (Simplified)
# -----------------------------
def recursive_summarize(text):
    chunks = split_text(text)
    summary = ""

    for chunk in chunks:
        summary = base_summarizer.invoke({
            "text": summary + "\n" + chunk
        })

    return summary

# -----------------------------
# STEP 8: Routing Logic (IMPORTANT CONCEPT)
# -----------------------------
def is_long(text):
    return len(text) > 4000  # simple approximation

# -----------------------------
# STEP 9: Build Pipeline
# -----------------------------
pipeline = (
    RunnableLambda(extract_transcript)
    | RunnableBranch(
        (RunnableLambda(is_long), RunnableLambda(recursive_summarize)),
        RunnableLambda(lambda x: base_summarizer.invoke({"text": x}))
    )
)

# -----------------------------
# STEP 10: Run App
# -----------------------------
import streamlit as st

st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon="🎥"
)

st.title("🎥 YouTube Summarizer")

video_url = st.text_input(
    "Enter YouTube Video URL"
)

if st.button("Generate Article"):

    if video_url:

        with st.spinner("Generating summary..."):

            result = pipeline.invoke(video_url)

        st.success("Done!")

        st.markdown(result)

    else:
        st.warning("Please enter a YouTube URL")

# =============================
# HOW TO EXPLAIN THIS IN INTERVIEW
# =============================

# 1. I extract transcript from YouTube
# 2. I check if content is long or short
# 3. If short → direct summarization
# 4. If long → split into chunks and summarize step-by-step
# 5. I used RunnableBranch for dynamic routing
# 6. Finally, I generate a structured article using LLM