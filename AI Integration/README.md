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

Gemini 2.0 Flash was my choice of integration into my chatbot, as it offers built-in functionality for uploading documents directly through the API, thereby simplifying document Q&A chatbot development. Google AI Studio offers the ability to use Gemini 2.0 Flash free of charge; it is an excellent resource for student-based projects. The model does an excellent job at reading the content of PDF files and text documents; therefore, it was perfect for our application.

---

## Agile Process

- **Sprint 1:** Built the basic Streamlit UI and file uploader
- **Sprint 2:** Connected the Google Gemini API and got document uploads working
- **Sprint 3:** Added chat history so the conversation stays on screen
- **Sprint 4:** Fixed bugs and tested with different documents

---

## Ethical Reflection

Using AI tools is valuable, but care must be taken to use the tools properly. One of the concerns with Gemini is that some of the answers may be incorrect, especially in instances in which the model appears to be very confident in the response, so it is recommended that you confirm all important information. Additionally, there is the issue of privacy because any files uploaded go to Google's servers, so avoid uploading anything personal or confidential. I added a prompt telling the model to only respond using the uploaded file, which reduces answers that are made up or fabricated. As with any tool, AI has great potential, but users must remain critical about their use and not accept answers quite blindly.
