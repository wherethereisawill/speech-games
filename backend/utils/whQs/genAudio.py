# uv run -m utils.whQs.genAudio

from lib.elevenlabs import elevenlabs_client
from utils.saveAudio import save_audio

def generate_11labs_audio_bytes(text: str) -> bytes:
    audio_bytes = b""
    try:
        for chunk in elevenlabs_client.text_to_speech.convert(
            voice_id="SAz9YHcvj6GT2YYXdXww",
            output_format="mp3_44100_128",
            text=text,
            model_id="eleven_multilingual_v2"
        ):
            audio_bytes += chunk
        return audio_bytes
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    import time
    text = "Who is the main character in the story?"
    audio_bytes = generate_11labs_audio_bytes(text)
    if audio_bytes is None:
        print("No audio bytes returned")
        exit()

    timestamp = int(time.time())
    file_name = f"{timestamp}.mp3"
    file_dir = "/Users/willnorris/Documents/Projects/speech-games/backend/utils/whQs/audio"
    save_audio(audio_bytes, file_name, file_dir)