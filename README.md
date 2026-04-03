# Youtube-Summarizer
YouTube Summarizer using Generative AI with Streamlit UI.
Overview

The YouTube Summarizer is a Generative AI application that extracts transcripts from YouTube videos and converts them into concise summaries and structured article-style content.

This project demonstrates an end-to-end Generative AI pipeline including transcript extraction, LLM-based summarization, and article generation using a Streamlit web interface.

Features
Extract transcript from YouTube videos
Generate AI-powered summaries
Convert summaries into structured articles
Streamlit-based user interface
Download article as HTML
Handles long videos using text chunking
Tech Stack
Python
Streamlit
Generative AI (LLM API)
OpenRouter API
YouTube Transcript API
Natural Language Processing (NLP)
Project Structure
youtube_summarizer/
│
├── app.py
├── main.py
├── transcript.py
├── summarizer.py
├── article_generator.py
├── requirements.txt
├── README.md
├── .gitignore
Installation
1. Clone the repository
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
2. Install dependencies
pip install -r requirements.txt
3. Create .env file

Create a .env file in the project folder and add:

OPENROUTER_API_KEY=your_api_key_here
4. Run the application
streamlit run app.py

The application will open in your browser.

How It Works
Enter YouTube URL
Extract transcript
Generate summary using AI
Convert summary into article
Display output
Download HTML file
Future Improvements
Multi-language support
PDF export option
Automatic video title detection
Deploy to Streamlit Cloud
Author

Pavani Vutukuru
Data Science | Generative AI Enthusiast
