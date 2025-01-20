import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
client_id = "daccc75eac95417bb1a7d6af713569ec"
client_secret = "f63aad051b0748f7b51de83f97aef31f"
redirect_uri = "http://localhost:8888/callback"

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope="user-library-read user-read-playback-state user-modify-playback-state"))

# Device ID obtained earlier (replace with your actual device ID)
device_id = '193d3482d8fb5f2f3f5796606722f1d4b6bb5acb'

# Function to start playback
def start_playback():
    sp.start_playback(device_id=device_id)

# Function to play a specific track (replace with your track URI)
def play_song():
    track_uri = 'spotify:track:YOUR_TRACK_URI'
    sp.start_playback(device_id=device_id, uris=[track_uri])

# Call the play_song function to start playback
play_song()
