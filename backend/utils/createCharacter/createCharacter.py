# uv run -m utils.whQs.whoImage
from lib.gemini import google_client
from utils.saveImage import save_image
from PIL import Image

def gen_image(prompt: str) -> bytes:

    pose_ref = Image.open("/Users/willnorris/Documents/Projects/speech-games/backend/utils/createCharacter/files/pose4.png")
    
    response = google_client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt, pose_ref],
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            return part.inline_data.data

if __name__ == "__main__":
    import time
    timestamp = int(time.time())
    prompt = """You are an expert childrens character artist. 
    Posed according to the reference image, create an image of a character with a resemblance to an octopus.
    The background of the image should be a single block colour which is complementary to the colour of the character.  
    The aesthetics for the character/image should be 3D stylized animation in the style of modern feature animation films 
    - blending realism in textures and lighting with cartoon exaggeration in anatomy and expressions."""
    image_bytes = gen_image(prompt)
    if image_bytes is None:
        print("No image bytes returned")
        exit()
    image_name = f"{timestamp}.png"
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/utils/createCharacter/images"
    save_image(image_bytes, image_name, file_dir)