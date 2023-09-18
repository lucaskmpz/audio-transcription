import os
import openai
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import io
from pydub import AudioSegment
import tempfile

# Initialize your FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# Configure your OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Function to transcribe audio using OpenAI API


def transcription(audio_file) -> str:
    response = openai.Audio.transcribe(
        "whisper-1", file=audio_file)

    return response['text']

# Endpoint to handle audio file upload and transcription


@app.post(
    path="/api/transcribe",
)
async def transcribe_audio(file: UploadFile):
    """
    Receive and transcribe an audio file
    """
    # Read the uploaded MP3 binary audio content
    mp3_content = await file.read()

    # Convert MP3 binary content to an AudioSegment object
    audio = AudioSegment.from_file(io.BytesIO(mp3_content), format="mp3")

    # Save the AudioSegment to a temporary MP3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_mp3_path = temp_file.name
        audio.export(temp_mp3_path, format="mp3")

    # Read the content of the temporary MP3 file
    with open(temp_mp3_path, "rb") as temp_mp3_file:
        # Transcribe the audio content
        audio_transcripted = transcription(temp_mp3_file)

    # Clean up the temporary MP3 file
    os.unlink(temp_mp3_path)

    # Return the audio transcript as JSON response
    return JSONResponse(content={"transcription": audio_transcripted})
