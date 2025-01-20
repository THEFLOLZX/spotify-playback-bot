import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

client_id = 'daccc75eac95417bb1a7d6af713569ec'  # Your client ID
client_secret = 'f63aad051b0748f7b51de83f97aef31f'  # Your client secret
redirect_uri = 'http://localhost:8888/callback'
refresh_token = 'AQCl56KQsjEZ1l2_H9oWUIUUreEQ7pqs76E0djig7NmDsN-iyU5xIaZ47dNfEx1-By9mbtxFvxF-4Mbma8YJCRSppY2_oZOm7gpvbrVp60qp-ssENiuKLlNTb1EEOtLHoOM'  # Your refresh token
playlist_uri = 'spotify:playlist:4beauqcBlaUMTmtsIucXeP'  # Replace with your playlist URI

# Initialize SpotifyOAuth to manage the authentication flow
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri)

def refresh_and_play():
    # Refresh the access token using the refresh token
    token_info = sp_oauth.refresh_access_token(refresh_token)
    access_token = token_info['access_token']

    # Set up the Spotify client with the new access token
    sp = spotipy.Spotify(auth=access_token)

    # Fetch available devices
    devices = sp.devices()

    # If no devices are found, notify the user
    if not devices['devices']:
        print("No available devices found.")
        return

    # Assuming you want to use the first available device (modify accordingly if you have multiple)
    device_id = devices['devices'][0]['id']
    print(f"Using device: {devices['devices'][0]['name']}")

    # Start playback of the playlist on the selected device
    sp.start_playback(device_id=device_id, context_uri=playlist_uri)
    print("Playback started on device:", devices['devices'][0]['name'])

# Run the bot continuously
while True:
    try:
        refresh_and_play()
        # Wait for 60 minutes before refreshing the token and starting the playback again
        time.sleep(60 * 60)  # 1 hour
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(60)  # Wait for 1 minute before retrying
