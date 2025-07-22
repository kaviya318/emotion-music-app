# music_player.py
import webbrowser

emotion_to_song = {
    "happy": "https://open.spotify.com/track/2JlzHPGIVaLNAppX1viq7f?si=69d86b07e6d845c4",
    "sad": "https://open.spotify.com/track/6old0mA1IHi5lw2yLv3ri6?si=8d249b6bdcb240f9",
    "angry": "https://open.spotify.com/track/3F7IiHst8X2KXwu4oBkywY?si=28ac3dbf621c4fa2",
    "neutral": "https://open.spotify.com/track/6OEY4EgyHxwJ8IhanTnvEL?si=6cacefa4bbde4479",
    "fear":"https://open.spotify.com/track/3Vb8KkT6Ub5fFGPYJCJyLh?si=271b5bb1dcfb4949",
    "surprise":"https://open.spotify.com/track/0pewR6RoxANQNJPgXTU8IG?si=982ac4104c064212"
}

def play_music_by_emotion(emotion):
    url = emotion_to_song.get(emotion)
    if url:
        print(f"🎵 Playing for emotion: {emotion}")
        webbrowser.open(url)
    else:
        print(f"No song found for emotion: {emotion}")
