# Audio Transcription App using OpenAI and FastAPI

Welcome to the Audio Transcription App! This repository contains a Python application that leverages the power of OpenAI and the FastAPI framework to transcribe audio files. With this app, you can easily upload MP3 audio files, which will then be converted into text using OpenAI's transcription model, providing you with the transcribed content.

## Technologies Used

This application is built on the following technologies:

- **Python**: A versatile programming language known for its simplicity and readability.
- **OpenAI API**: Utilized to transcribe audio content and convert it into text.
- **FastAPI**: A modern, fast, and highly performant web framework for building APIs with Python.
- **pydub**: A library for audio file manipulation, used to handle audio conversion and processing.
- **tempfile**: A built-in Python module used for managing temporary files.

## Prerequisites

Before you begin, ensure you have the following:

- **Python (>=3.6)** installed on your system.
- An **OpenAI API key**. If you don't have one, you can sign up and obtain an API key from the [OpenAI website](https://beta.openai.com/signup/).
- Basic familiarity with **FastAPI**, **OpenAI API**, audio file handling, and Python programming.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required Python packages using `pip`:

   ```bash
   pip install fastapi uvicorn openai pydub
   ```

3. Open the `main.py` file and replace `'OPENAI_API_KEY'` with your actual OpenAI API key.

## Usage

1. Run the FastAPI server using the following command:

   ```bash
   uvicorn main:app
   ```

2. Once the server is running, you can access the FastAPI documentation at `http://127.0.0.1:8000/docs`. Here, you can test the `/api/transcribe` endpoint by uploading an MP3 audio file.

3. The uploaded audio file will be transcribed using the OpenAI API, and the resulting transcription will be returned as a JSON response.

## How It Works

1. When you upload an MP3 file to the `/api/transcribe` endpoint, the application reads the binary content of the audio file.

2. The binary content is converted into an `AudioSegment` object using the `pydub` library, which makes the audio data suitable for processing.

3. The `AudioSegment` is temporarily saved as an MP3 file using the `tempfile.NamedTemporaryFile` function.

4. The temporary MP3 file's content is read and passed to the `transcription` function, which sends an API call to the OpenAI transcription model via the OpenAI Python library.

5. The transcription response is extracted from the API response and returned as a JSON response to the user.

6. The temporary MP3 file is cleaned up by deleting it.
