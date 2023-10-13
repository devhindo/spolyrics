"""spotipy library for Spotify API calls"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from env import CLIENT_ID, CLIENT_SECRET


def auth():
    """Authenticates the user using the Spotify API"""
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri="https://github.com/devhindo/spolyrics",
            scope="user-library-read",
        )
    )

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results["items"]):
        track = item["track"]
        print(idx, track["artists"][0]["name"], " – ", track["name"])
