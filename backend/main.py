# cd backend
# uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

from utils.whQs.genQs import gen_qs
from utils.whQs.genImage import gen_image
from utils.whQs.genAudio import generate_11labs_audio_bytes
import base64

@app.get("/create-wh-q")
def create_wh_q(age: int, interests: str):
    try:
        # Generate WH questions and scene
        result = gen_qs(age=age, interests=interests)

        # Generate image bytes and encode as base64 data URL
        image_bytes = gen_image(
            scene_description=result["scene_description"],
            who=result["who"],
            what=result["what"],
            when=result["when"],
            where=result["where"],
            why=result["why"],
            how=result["how"],
        )
        image_base64 = f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"

        # Generate audio bytes for each text and encode as base64 data URLs
        audio_scene_description = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['scene_description'])).decode('utf-8')}"
        audio_who = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['who'])).decode('utf-8')}"
        audio_what = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['what'])).decode('utf-8')}"
        audio_when = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['when'])).decode('utf-8')}"
        audio_where = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['where'])).decode('utf-8')}"
        audio_why = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['why'])).decode('utf-8')}"
        audio_how = f"data:audio/mpeg;base64,{base64.b64encode(generate_11labs_audio_bytes(result['how'])).decode('utf-8')}"

        return {
            **result,
            "image_base64": image_base64,
            "audio": {
                "scene_description": audio_scene_description,
                "who": audio_who,
                "what": audio_what,
                "when": audio_when,
                "where": audio_where,
                "why": audio_why,
                "how": audio_how,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))