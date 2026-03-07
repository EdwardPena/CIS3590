# AI Document Assistant

A simple Streamlit chatbot where you upload a PDF or TXT file and ask questions about it. Powered by Google's Gemini AI.

---

## How to Run

1. Install dependencies:
   ```bash
   pip install streamlit google-genai python-dotenv
   ```

2. Create a `.env` file and add your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. Run the app:
   ```bash
   streamlit run aiBot.py
   ```

---

## Model Name & Source

- **Model:** `gemini-2.0-flash`
- **Provider:** Google (via Google AI Studio)
- **SDK:** `google-genai` Python package

---

## Why I Chose This Model

I chose Gemini 2.0 Flash because it has built-in support for uploading documents directly through the API, which made building a document Q&A chatbot much simpler. It's also free to use through Google AI Studio, which is great for a student project. The model handles reading and understanding PDFs and text files well, which is exactly what this app needs.

---

## Agile Process

- **Sprint 1:** Built the basic Streamlit UI and file uploader
- **Sprint 2:** Connected the Google Gemini API and got document uploads working
- **Sprint 3:** Added chat history so the conversation stays on screen
- **Sprint 4:** Fixed bugs and tested with different documents

---

## Ethical Reflection

AI tools like this one are useful, but it's important to use them responsibly. One concern is that Gemini can sometimes give wrong answers even when it sounds confident, so users should double-check important information. Another issue is privacy — when you upload a document, it gets sent to Google's servers, so you should avoid uploading anything sensitive or personal. I added a system prompt that tells the model to only answer from the uploaded file, which helps reduce made-up responses. Overall, AI is a powerful tool, but users need to stay critical and not blindly trust everything it says.
