# uv run -m utils.whQs.genImage
from lib.gemini import google_client
from utils.saveImage import save_image

def gen_image(scene_description: str, who: str, what: str, when: str, where: str, why: str, how: str) -> bytes:

    prompt = create_prompt(scene_description, who, what, when, where, why, how)
    
    response = google_client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt],
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            return part.inline_data.data
        
base_prompt = """
You are an expert childrens character artist & illustrator.
You are tasked with creating an illustrated image for a childrens book which describes the following scene: {scene_description}.
Children will play a game where they read the scene and answer the following WH-questions: {who}, {what}, {when}, {where}, {why}, {how}.
Do not include any text in the image. The image should only visually show the character and the answers to the WH-questions.
The aesthetics for the character/image should be 3D stylized animation in the style of modern feature animation films 
- blending realism in textures and lighting with cartoon exaggeration in anatomy and expressions.
"""
        
def create_prompt(scene_description: str, who: str, what: str, when: str, where: str, why: str, how: str):
    return base_prompt.format(scene_description=scene_description, who=who, what=what, when=when, where=where, why=why, how=how)

if __name__ == "__main__":
    import time
    timestamp = int(time.time())
    scene_description = "In a sunny farm meadow, little Eli the kind tractor chugged past cows and horses, his wheels splashing gently through friendly mud like puddles of chocolate. He found a tiny toy dinosaur stuck in the ooze and hummed a brave song as he tugged it free with his strong, muddy tires. The cows mooed a thank-you chorus, and Eli’s headlight eyes twinkled like morning stars."
    who = "Who is the main character in the story?"
    what = "What does Eli pull out of the mud?"
    when = "When does Eli shine his headlight eyes—day or night?"
    where = "Where is Eli driving?"
    why = "Why does Eli pull the tiny dinosaur from the mud?"
    how = "How does Eli move through the muddy puddles?"
    image_bytes = gen_image(scene_description, who, what, when, where, why, how)
    if image_bytes is None:
        print("No image bytes returned")
        exit()
    image_name = f"{timestamp}.png"
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/utils/whQs/images"
    save_image(image_bytes, image_name, file_dir)