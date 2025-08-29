# uv run -m lib.gemini

from dotenv import load_dotenv
from google import genai

load_dotenv()

google_client = genai.Client()

if __name__ == "__main__":

    response = google_client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)