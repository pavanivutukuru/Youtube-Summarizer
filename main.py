from transcript import get_transcript
from summarizer import summarize_text
from article_generator import generate_article
import markdown


def save_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def main():

    video_url = input("Enter YouTube URL: ")

    print("Extracting transcript...")
    transcript = get_transcript(video_url)

    save_file("transcript.txt", transcript)

    print("Generating summary...")
    summary = summarize_text(transcript)

    save_file("summary.txt", summary)

    print("Generating article...")
    article = generate_article(summary)

    save_file("article.md", article)

    html = markdown.markdown(article)

    save_file("article.html", html)

    print("Project Completed Successfully!")


if __name__ == "__main__":
    main()