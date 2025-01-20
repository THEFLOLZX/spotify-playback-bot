import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set your Spotify credentials
client_id = "daccc75eac95417bb1a7d6af713569ec"
client_secret = "f63aad051b0748f7b51de83f97aef31f"
redirect_uri = "http://localhost:8888/callback"

# Create the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope="user-library-read user-modify-playback-state user-read-playback-state")

# Check for an existing token in the environment (use .env or a secure method for storing tokens)
token_info = sp_oauth.get_cached_token()

if not token_info:
    # If there's no token cached, we need to get a new token
    auth_url = sp_oauth.get_authorize_url()
    print(f"Go to the following URL and paste the resulting code here: {auth_url}")
    auth_code = input("Enter the code from the URL: ")
    token_info = sp_oauth.get_access_token(auth_code)

# Initialize Spotipy with the token
sp = spotipy.Spotify(auth=token_info['access_token'])

# Save the token for future use (you can persist it to an environment variable or a file)
# Example: save to a file or environment variable
# os.environ['SPOTIPY_TOKEN'] = token_info['access_token']

# Now, you can interact with the Spotify API
def play_song():
    device_id = 'YOUR_DEVICE_ID'
    track_uri = 'YOUR_PLAYLIST_URI'
    sp.start_playback(device_id=device_id, uris=[track_uri])

play_song()
