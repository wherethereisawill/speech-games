# uv run -m utils.soundStory.genImage
from lib.gemini import google_client
from utils.saveImage import save_image

def gen_image(prompt: str) -> bytes:

    response = google_client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt],
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            return part.inline_data.data

if __name__ == "__main__":
    prompt = "Create a photorealistic picture of a lion stood on a mountain wearing a crown."
    image_bytes = gen_image(prompt)
    image_name = "test.png"
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/utils/soundStory/images"
    save_image(image_bytes, image_name, file_dir)