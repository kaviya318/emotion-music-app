# 🎵 Real-Time Emotion Detection and Genre-Based Music Playback

This project uses **Deep Learning** and **Spotify API** to detect a user's facial emotion in real-time and play a matching genre-based song. It combines computer vision (via OpenCV and Keras) with real-time webcam input and music streaming.

---

## 👩‍💻 Developed by:
**Kaviya**  
💡 Final Year Project – 2025  

---

## 📸 Features

- ✅ Real-time face & emotion detection using webcam
- 🎯 Emotion classification using `emotion_model.h5` (mini_XCEPTION)
- 🔁 Detects only once per run (no repeated detections)
- ❓ Asks user: *“Do you want to play a song for this emotion?”*
- 🎵 On user click → Plays a Spotify song matching the emotion (e.g., sad → soft song, happy → upbeat music)

---

## 🧠 Emotions Detected

- 😠 Angry
- 😞 Sad
- 😄 Happy
- 😐 Neutral

---

## 🛠️ Technologies Used

- Python 3.11
- TensorFlow & Keras
- OpenCV
- Flask
- Spotipy (Spotify Web API)
- HTML + CSS (for frontend)

---

## ▶️ How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt

---

## 📁 Project Folder Structure

emotion_music_project/
│
├── app.py # Main Flask app
├── emotion_model.h5 # Pre-trained emotion detection model (mini_XCEPTION)
├── music_player.py # Maps emotion to music
├── spotify_auth.py # Spotify API login handler
├── requirements.txt # All Python dependencies
├── LICENSE # MIT license (your name)
├── templates/
│ └── index.html # Web UI for webcam + song button
└── static/
└── style.css # Optional styling


