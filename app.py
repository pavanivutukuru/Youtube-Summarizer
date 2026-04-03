import streamlit as st
from transcript import get_transcript
from summarizer import summarize_text
from article_generator import generate_article
import markdown

st.title("🎥 YouTube Summarizer")

video_url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):

    if video_url:

        st.write("Extracting transcript...")
        transcript = get_transcript(video_url)

        st.write("Generating summary...")
        summary = summarize_text(transcript)

        st.subheader("Summary")
        st.write(summary)

        st.write("Generating article...")
        article = generate_article(summary)

        st.subheader("Article")
        st.markdown(article)

        html = markdown.markdown(article)

        st.download_button(
            label="Download HTML",
            data=html,
            file_name="article.html",
            mime="text/html"
        )

    else:
        st.warning("Please enter YouTube URL")