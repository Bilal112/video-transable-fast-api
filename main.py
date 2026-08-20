import os
import torch
import gradio as gr
from yt_dlp import YoutubeDL
from faster_whisper import WhisperModel

# Detect CUDA (GPU) automatically to prevent RuntimeError
device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if device == "cuda" else "int8"

print(f"Running on device: {device}")

# Load model cleanly
model = WhisperModel("tiny", device=device, compute_type=compute_type)

def transcribe(url):
    if not url:
        return "Video URL enter karein."
        
    output_file = "temp_audio.mp3"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        segments, _ = model.transcribe(output_file)
        return " ".join([s.text for s in segments])
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if os.path.exists(output_file):
            os.remove(output_file)

demo = gr.Interface(fn=transcribe, inputs="text", outputs="text", title="Free AI Transcriber")
demo.launch(share=True)