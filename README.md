

# 🧠 AI-Based Text Summarization System

## 📌 Description

This project is an AI-powered text summarization system that generates short and meaningful summaries from long text or PDF documents using Natural Language Processing (NLP) and transformer-based models.

It uses the T5-small model from Hugging Face to process and summarize text efficiently. The system also handles large input text using a chunking technique.

---

## 🚀 Features

* Summarizes long text into concise output
* Supports PDF document input
* Handles large text using chunking
* Chat-style user interface using Streamlit
* Displays word count comparison
* Simple and interactive UI

---

## 🛠️ Tech Stack

**Programming Language:**

* Python

**AI / NLP:**

* Hugging Face Transformers
* T5-small model

**Frontend / UI:**

* Streamlit

**PDF Processing:**

* pypdf

**Backend:**

* Python (tokenization, chunking, summarization logic)

---

## 📂 Project Structure

AI-Text-Summarizer/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
│
└── utils/
    ├── summarizer.py       # Summarization logic
    └── pdf_reader.py       # PDF extraction logic

---

## 🔄 How It Works

1. User enters text or uploads a PDF
2. Text is extracted and cleaned
3. Large text is split into smaller chunks
4. Each chunk is summarized using T5 model
5. All summaries are combined
6. Final refined summary is generated
7. Output is displayed in the UI

---

## ▶️ How to Run

1. Clone the repository
   git clone [https://github.com/mansipawar13/ai-text-summarizer.git](https://github.com/mansipawar13/ai-text-summarizer.git)

2. Go to the project folder
   cd ai-text-summarizer

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   streamlit run app.py

---

## ⚠️ Limitations

* Slow for very large PDFs
* Depends on model accuracy
* Requires internet for first-time model download
* T5-small provides moderate accuracy

---

## 🚀 Future Improvements

* Use advanced models like BART or Pegasus
* Add multi-language support
* Add speech-to-text feature
* Improve UI design
* Add option to download summary

---

## 🎯 Use Cases

* Summarizing study material
* Understanding long documents quickly
* Content summarization for blogs/articles

---

## 📌 Author

Mansi Pawar

---


