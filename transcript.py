from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    return match.group(1)


def get_transcript(video_url):
    video_id = extract_video_id(video_url)

    transcript_list = YouTubeTranscriptApi().fetch(
        video_id,
        languages=["en", "en-US", "hi"]
    )

    text = " ".join([item.text for item in transcript_list])

    return text
