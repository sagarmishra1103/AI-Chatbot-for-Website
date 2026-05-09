import streamlit as st
import time

from components.url_mode_web_scrap import scrape_website
from components.context_builder import build_chunks
from components.retriever import get_top_chunks
from components.prompt_engine import build_prompt
from components.gemini_client import generate_response
from utils.logger import log

st.set_page_config(page_title="AI Chatbot", layout="wide")

# ---------------- SESSION ----------------
if "cache" not in st.session_state:
    st.session_state.cache = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "logs" not in st.session_state:
    st.session_state.logs = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("Controls")

url = st.sidebar.text_input("Enter URL")

if st.sidebar.button("Process URL"):
    try:
        start = time.time()

        if url in st.session_state.cache:
            chunks = st.session_state.cache[url]
            st.session_state.logs.append(log("Cache hit"))
        else:
            text = scrape_website(url)
            chunks = build_chunks(text)
            st.session_state.cache[url] = chunks
            st.session_state.logs.append(log(f"Scraped + {len(chunks)} chunks"))

        st.session_state.chunks = chunks
        st.session_state.logs.append(log(f"Done in {round(time.time()-start,2)}s"))

    except Exception as e:
        st.error(str(e))

# Debug Panel
st.sidebar.subheader("Debug")
st.sidebar.write(f"Chunks: {len(st.session_state.get('chunks', []))}")
for l in st.session_state.logs[-5:]:
    st.sidebar.write(l)

# ---------------- MAIN ----------------
st.title("💬 Website Chatbot")
# ---------------- CHUNK VIEWER ----------------
st.markdown("---")

if "chunks" in st.session_state:
    if st.button("📂 Show Chunked Data"):

        chunk_text = "\n\n----------------------\n\n".join(
            [f"Chunk {i+1}:\n{chunk}" for i, chunk in enumerate(st.session_state.chunks)]
        )

        st.text_area(
            "Chunked Data (Scrollable)",
            value=chunk_text,
            height=200,   # ~3–4 lines visible minimum
        )

# ---------------- INPUT AT TOP ----------------
question = st.text_input("Ask a question", key="input_box")

ask = st.button("Ask")

st.markdown("---")

# ---------------- CHAT DISPLAY ----------------
for role, msg in st.session_state.chat_history:
    if role == "User":
        st.markdown(
            f"""
            <div style='background-color:#7F2020;padding:10px;border-radius:10px;margin:5px 0;color:white'>
            <b>You:</b> {msg}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <>
            <div style='background-color:#869B7E;padding:10px;border-radius:10px;margin:5px 0;color:white'>
            <b>AI:</b> 
            {msg}
            </div>
            </>
            """,
            unsafe_allow_html=True
        )

# ---------------- RESPONSE LOGIC ----------------
if ask:
    if "chunks" not in st.session_state:
        st.warning("Process URL first")
    else:
        start = time.time()

        with st.spinner("Thinking..."):
            # force minimum 3 seconds spinner
            spinner_start = time.time()

            top_chunks = get_top_chunks(question, st.session_state.chunks)
            prompt = build_prompt(question, top_chunks, st.session_state.chat_history)
            answer = generate_response(prompt)

            # enforce minimum delay
            elapsed = time.time() - spinner_start
            if elapsed < 3:
                time.sleep(3 - elapsed)

        st.session_state.chat_history.append(("User", question))
        st.session_state.chat_history.append(("AI", answer))

        st.session_state.logs.append(log(f"Answered in {round(time.time()-start,2)}s"))

        st.rerun()