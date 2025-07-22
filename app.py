from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
import threading
import os
import sys
import platform  # ✅ Import for Python version
from music_player import play_music_by_emotion

app = Flask(__name__)

# Base path for PyInstaller compatibility
base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))

# Load emotion detection model
model_path = os.path.join(base_path, 'emotion_model.h5')
model = load_model(model_path, compile=False)

# Emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Haar Cascade path
cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)

# Webcam
cap = cv2.VideoCapture(0)

# Global vars
detected_emotion = None
emotion_locked = False

def gen_frames():
    global detected_emotion, emotion_locked
    while True:
        success, frame = cap.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if not emotion_locked:
            for (x, y, w, h) in faces:
                roi = gray[y:y + h, x:x + w]
                roi = cv2.resize(roi, (48, 48))
                roi = roi.astype("float") / 255.0
                roi = np.reshape(roi, (1, 48, 48, 1))

                preds = model.predict(roi)
                detected_emotion = emotion_labels[np.argmax(preds)]

                # Draw box and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, detected_emotion, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)

                print(f"✅ Emotion detected: {detected_emotion}")
                emotion_locked = True
                break
        else:
            # Show locked emotion
            cv2.putText(frame, f"Emotion: {detected_emotion}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    python_version = platform.python_version()  # ✅ Get Python version
    return render_template('index.html', emotion=detected_emotion, python_version=python_version)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_emotion')
def get_emotion():
    return jsonify({'emotion': detected_emotion})

@app.route('/play_song')
def play_song():
    if detected_emotion:
        play_music_by_emotion(detected_emotion)
        return jsonify({'status': 'playing'})
    return jsonify({'status': 'no_emotion'})

if __name__ == '__main__':
    print("✅ Python version:", platform.python_version())  # ✅ Terminal output
    print("✅ App running at http://127.0.0.1:5000")
    app.run(debug=True)
