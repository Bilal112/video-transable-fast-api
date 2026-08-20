# 🎙️ Fast & Free AI Video Transcriber

An automated, open-source AI video-to-text transcription service built using **Python**, **FastAPI**, **yt-dlp**, and **Faster-Whisper / Groq Cloud API**. This application allows users to extract audio from video URLs (e.g., YouTube) and convert speech to text with high accuracy and speed.

---

## ✨ Features

- ⚡ **Super-Fast Transcription:** Transcribes multi-minute videos within seconds using optimized local models or Groq Cloud hardware acceleration.
- 🎯 **High Accuracy:** Leverages OpenAI's Whisper model architecture (supports English, Urdu, Hindi, Hinglish, and 90+ other languages).
- 🔓 **100% Free & Open-Source:** No mandatory paid API keys or subscriptions required.
- 🛠️ **Dual Engine Support:**
  - **Local Mode:** Runs `faster-whisper` directly on CPU/GPU without external services.
  - **Cloud Mode:** Uses Groq's free tier for lightning-fast serverless Whisper-Large-v3 processing.
- 🌐 **Multiple Deployment Options:** Ready to deploy on **Hugging Face Spaces**, **Render**, **Kaggle**, or **Google Colab**.

---

## 🏗️ Project Architecture & File Structure

```text
video-transcriber/
├── app.py              # Main FastAPI / Gradio application script
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration (FFmpeg + Python runtime)
└── README.md           # Documentation
```

---

## 🚀 Quickstart (Local Setup)

### Prerequisites
- **Python 3.10+** installed.
- **FFmpeg** installed on your system (required for audio extraction).

#### Installing FFmpeg:
- **macOS:** `brew install ffmpeg`
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install -y ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to system PATH.

---

### Step-by-Step Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/video-transcriber.git
   cd video-transcriber
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   * **Option A: Run FastAPI Server (Swagger Interactive UI)**
     ```bash
     uvicorn app:app --reload
     ```
     Access Swagger documentation at: `http://127.0.0.1:8000/docs`

   * **Option B: Run Gradio UI Web App**
     ```bash
     python app.py
     ```
     Open the displayed local link in your browser (`http://127.0.0.1:7860`).

---

## 📦 Dependencies (`requirements.txt`)

```text
fastapi
uvicorn
pydantic
yt-dlp
faster-whisper
gradio
groq
```

---

## 🌐 Deployment Options

### Option 1: Hugging Face Spaces (Recommended - Free 16GB RAM)

Hugging Face Spaces offers a generous free tier (16GB RAM, 2 vCPU), ideal for running local Whisper models without memory crashes.

1. Create a new Space at [huggingface.co/new-space](https://huggingface.co/new-space).
2. Choose **SDK: Gradio** (or **Docker** if deploying the FastAPI version).
3. Select **Hardware: CPU Basic (16GB RAM - Free)**.
4. Upload `app.py` and `requirements.txt`.
5. Commit changes. Your app will automatically build and launch!

---

### Option 2: Deploy to Render (Serverless Mode)

Since Render's free tier has a 512MB RAM limit, run the app using the **Groq Free Whisper API** integration to avoid out-of-memory errors:

1. Obtain a free API key from [console.groq.com](https://console.groq.com/).
2. Push your repo to GitHub.
3. Create a **New Web Service** on [Render](https://render.com).
4. Set Environment Variable: `GROQ_API_KEY = your_key_here`.
5. Deploy as a Docker or Python service.

---

### Option 3: Free GPU Notebooks (Google Colab / Kaggle)

For temporary, high-speed GPU execution:

1. Open Google Colab or Kaggle Notebook.
2. Enable **T4 GPU Accelerator** in runtime settings.
3. Install packages:
   ```bash
   !pip install yt-dlp faster-whisper gradio
   ```
4. Run the Gradio script with `demo.launch(share=True)` to generate a temporary public URL (`https://xxxx.gradio.live`).

---

## ⚡ Model Size vs. Speed Reference

| Model | Memory Required | Speed | Recommended Use Case |
| :--- | :--- | :--- | :--- |
| **tiny** | ~75 MB | ⚡⚡⚡ Ultra Fast | Fast testing, clear audio |
| **base** | ~145 MB | ⚡⚡ Fast | Standard English audio |
| **small** | ~480 MB | ⚖️ Balanced | Multi-language (Urdu, Hindi, accents) |
| **medium** | ~1.5 GB | 🐢 Slow | Complex / Noisy audio |
| **large-v3**| ~3 GB | 🐢 Slow (Local) / ⚡⚡ Fast (Groq) | Maximum precision & transcription quality |

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to modify and distribute as needed.
