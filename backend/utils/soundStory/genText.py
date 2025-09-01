# uv run -m utils.generateSoundStory
from lib.openai import openai_client

def generate_sound_story(prompt: str) -> str:
    response = openai_client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "minimal"},
        input=prompt
    )
    return response.output_text

if __name__ == "__main__":
    prompt = "You are a famous children's author known for their creative, funny and engaging stories. Write a 50-word auditory bombardment story with a space theme for a 6-year-old featuring the /s/ sound. The story should include ~5 words with the /s/ sound. The story must be suitable for a 5-year old."
    story = generate_sound_story(prompt)
    print(story)