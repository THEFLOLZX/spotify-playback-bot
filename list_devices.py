import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify credentials
client_id = "daccc75eac95417bb1a7d6af713569ec"
client_secret = "f63aad051b0748f7b51de83f97aef31f"
redirect_uri = "http://localhost:8888/callback"

# Initialize the Spotify client with user authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read user-read-playback-state user-read-currently-playing"))

# Fetch available devices
devices = sp.devices()

# Check the response from the API
print(devices)

# Print all available devices and their IDs
if 'devices' in devices:
    for device in devices['devices']:
        print(f"Device Name: {device['name']}, Device ID: {device['id']}")
else:
    print("No devices found.")
