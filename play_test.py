import webbrowser

# Simulate an emotion (you can change this later to real-time emotion)
emotion = "happy"

# Emotion-to-song link mapping (add more if needed)
emotion_to_spotify_link = {
    "happy": "https://open.spotify.com/track/6OEY4EgyHxwJ8IhanTnvEL",
    "sad": "https://open.spotify.com/track/3KkXRkHbMCARz0aVfEt68P",
    "angry": "https://open.spotify.com/track/3cHyrEgdyYRjgJKSOiOtcS",
    "neutral": "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b"
}

# Get song link based on emotion
song_link = emotion_to_spotify_link.get(emotion)

if song_link:
    print(f"🎧 Emotion detected: {emotion}")
    print("🔗 Opening Spotify song in browser...")
    webbrowser.open(song_link)
else:
    print(f"No song found for emotion: {emotion}")
