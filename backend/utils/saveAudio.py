import os

def save_audio(audio_bytes: bytes, filename: str, path: str):
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    with open(filepath, "wb") as f:
        f.write(audio_bytes)
    return filepath