# uv run -m utils.generateImage
from lib.gemini import google_client
import os

def generate_image(prompt: str) -> bytes:

    response = google_client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt],
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            return part.inline_data.data
        
def save_image(image: bytes, image_name: str):
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/files"
    os.makedirs(file_dir, exist_ok=True)
    save_path = os.path.join(file_dir, image_name)
    with open(save_path, "wb") as f:
        f.write(image)
    print(f"Saved image to {save_path}")

if __name__ == "__main__":
    prompt = "Create a photorealistic picture of a lion stood on a mountain wearing a crown."
    image = generate_image(prompt)
    save_image(image, "generated_image_3.png")