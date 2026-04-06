import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pypdf import PdfReader

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Summarizer", layout="centered")

# ------------------ TITLE ------------------
st.title("AI Text Summarizer")
st.caption("Chat-style summarization with progress tracking")

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    return tokenizer, model

tokenizer, model = load_model()

# ------------------ FUNCTIONS ------------------
def summarize_with_progress(text):
    words = text.split()
    max_chunk = 400
    chunks = [" ".join(words[i:i+max_chunk]) for i in range(0, len(words), max_chunk)]

    summaries = []
    progress_bar = st.progress(0)

    for i, chunk in enumerate(chunks):
        inputs = tokenizer.encode(
            "summarize: " + chunk,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )

        summary_ids = model.generate(
            inputs,
            max_length=120,
            min_length=40,
            num_beams=4
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

        progress_bar.progress((i + 1) / len(chunks))

    # Combine
    combined = " ".join(summaries)

    inputs = tokenizer.encode(
        "summarize: " + combined,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    final_ids = model.generate(
        inputs,
        max_length=150,
        min_length=60,
        num_beams=4
    )

    return tokenizer.decode(final_ids[0], skip_special_tokens=True)


def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# ------------------ SESSION STATE ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ------------------ INPUT METHOD ------------------
option = st.radio("Choose Input Method:", ("Enter Text", "Upload PDF"))

if option == "Enter Text":
    user_text = st.text_area("Enter your text:", height=200)

elif option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        user_text = extract_pdf_text(uploaded_file)
        st.success("File loaded successfully")
    else:
        user_text = ""

# ------------------ BUTTONS ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize"):
        if user_text.strip() == "":
            st.warning("Please provide input")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_with_progress(user_text)

                # Word count
                before_words = len(user_text.split())
                after_words = len(summary.split())

                # Store chat
                st.session_state.chat.append({
                    "input": user_text,
                    "output": summary,
                    "before": before_words,
                    "after": after_words
                })

with col2:
    if st.button("Reset"):
        st.session_state.chat = []
        st.rerun()

# ------------------ CHAT UI ------------------
for item in reversed(st.session_state.chat):
    
    # User message
    with st.chat_message("user"):
        st.write(item["input"][:500] + "...")

    # AI response
    with st.chat_message("assistant"):
        st.write(item["output"])

        st.caption(f"Word count: {item['before']} → {item['after']}")