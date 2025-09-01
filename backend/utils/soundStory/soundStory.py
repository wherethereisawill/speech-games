# uv run -m utils.soundStory.soundStory

from utils.soundStory.genText import gen_text
from utils.soundStory.genImage import gen_image
from utils.saveImage import save_image
import time

def generate_sound_story_with_image():
    story_prompt = "You are a famous children's author known for their creative, funny and engaging stories. Write a 25-word auditory bombardment story with a space theme for a 6-year-old featuring the /s/ sound. The story should include maximum 5 words with the /s/ sound."
    story = gen_text(story_prompt)
    print(story)

    image_prompt = f"Create an image which represents the story described in the following text: {story}"
    image = gen_image(image_prompt)

    timestamp = int(time.time())
    file_name = f"{timestamp}.png"
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/utils/soundStory/images"
    save_image(image, file_name, file_dir)

if __name__ == "__main__":
    generate_sound_story_with_image()