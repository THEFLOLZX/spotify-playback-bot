import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request

# Spotify credentials (replace with your actual credentials)
client_id = 'daccc75eac95417bb1a7d6af713569ec'
client_secret = 'f63aad051b0748f7b51de83f97aef31f'
redirect_uri = 'http://localhost:8888/callback'

# Initialize Flask app
app = Flask(__name__)

# Spotify OAuth setup
scope = "user-library-read user-modify-playback-state user-read-playback-state"
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

@app.route('/')
def home():
    return 'Spotify Playback Bot is running!'

@app.route('/callback')
def callback():
    # Get the auth code from Spotify redirect
    auth_code = request.args.get('code')
    
    # Get the token info (including the refresh token)
    token_info = sp_oauth.get_access_token(auth_code)
    refresh_token = token_info['refresh_token']
    
    return f'Your refresh token is: {refresh_token}'

# Start the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
