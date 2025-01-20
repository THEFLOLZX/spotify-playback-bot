from flask import Flask
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0906c26b3e8c4b9bb4e1c9a00b26172d",
                                                client_secret="f34b0d6dfb3e4b678790de470a8a57fc",
                                                redirect_uri="http://localhost:8888/callback"))

# Use the playlist ID you provided
playlist_uri = "spotify:playlist:4beauqcBlaUMTmtsIucXeP"  # Your playlist ID

@app.route('/')
def start_playing_music():
    # Start playback on the user's active device
    sp.start_playback(context_uri=playlist_uri)

    return "Music is now playing from your playlist!"

if __name__ == "__main__":
    # Automatically start playback when the app is deployed
    app.run(debug=False, host="0.0.0.0", port=80)
