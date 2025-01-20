import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve Spotify API credentials from environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:8888/callback")  # If you have a custom redirect URI

# Check if the credentials are loaded properly
if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Spotify API credentials are missing. Please set them in environment variables.")

# Set up the Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read playlist-read-private user-read-playback-state user-modify-playback-state"))

# Replace this with your actual playlist URI or ID
playlist_uri = 'spotify:playlist:4beauqcBlaUMTmtsIucXeP'

# Function to start playback of a playlist
def start_playback():
    try:
        # Start playback on your active device
        sp.start_playback(context_uri=playlist_uri)
        print("Playback started.")
    except Exception as e:
        print(f"Error starting playback: {e}")

# Function to handle playback (you can also add more logic like shuffle, etc.)
def control_playback():
    try:
        sp.start_playback(context_uri=playlist_uri)
        sp.shuffle(True)  # To shuffle playback
        print("Playback started with shuffle.")
    except Exception as e:
        print(f"Error controlling playback: {e}")

if __name__ == "__main__":
    control_playback()
