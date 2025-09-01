import os

# file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/files"

def save_image(image: bytes, file_name: str, file_dir: str):
    os.makedirs(file_dir, exist_ok=True)
    save_path = os.path.join(file_dir, file_name)
    with open(save_path, "wb") as f:
        f.write(image)
    print(f"Saved image to {save_path}")