# uv run -m utils.soundStory

from utils.generateSoundStory import generate_sound_story
from utils.generateImage import generate_image, save_image

def generate_sound_story_with_image():
    story_prompt = "You are a famous children's author known for their creative, funny and engaging stories. Write a 25-word auditory bombardment story with a space theme for a 6-year-old featuring the /s/ sound. The story should include maximum 5 words with the /s/ sound."
    
    story = generate_sound_story(story_prompt)
    print(story)

    image_prompt = f"Create an image which represents the story described in the following text: {story}"

    image = generate_image(image_prompt)
    save_image(image, "sound_story_2.png")

if __name__ == "__main__":
    generate_sound_story_with_image()