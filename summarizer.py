import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def chunk_text(text, chunk_size=4000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def summarize_text(text):

    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:

        prompt = f"""
        Summarize the following YouTube transcript:

        {chunk}
        """

        response = client.chat.completions.create(
            model="openrouter/auto",
            messages=[{"role": "user", "content": prompt}]
        )

        summaries.append(response.choices[0].message.content)

    return "\n".join(summaries)