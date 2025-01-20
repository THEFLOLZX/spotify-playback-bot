import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
CLIENT_ID = "daccc75eac95417bb1a7d6af713569ec"
CLIENT_SECRET = "f63aad051b0748f7b51de83f97aef31f"
REDIRECT_URI = "http://localhost:8888/callback"
PLAYLIST_URI = "spotify:playlist:4beauqcBlaUMTmtsIucXeP"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-modify-playback-state user-read-playback-state"
))

def start_playback():
    """Start playing the playlist."""
    sp.start_playback(context_uri=PLAYLIST_URI)
    sp.shuffle(True)  # Enable shuffle
    sp.repeat("context")  # Repeat the playlist

def ensure_playback():
    """Check if playback is running and restart if necessary."""
    playback = sp.current_playback()
    if not playback or not playback.get('is_playing'):
        print("Playback stopped, restarting...")
        start_playback()
    else:
        print("Playback is running.")

# Main loop
while True:
    try:
        ensure_playback()
        time.sleep(300)  # Check every 5 minutes
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(30)  # Retry after 30 seconds if an error occurs
