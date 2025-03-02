# Create a CSV of all songs in a Spotify playlist
#   March 2025
#
#    inputs:
#        playlist_id       ID of Spotify playlist to fetch songs from

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

csv_filename = "spotify_playlist.csv" # desired output file name

# Spotify API credentials (set up an app at https://developer.spotify.com/)
CLIENT_ID = 'your_client_id' # replace with your client ID
CLIENT_SECRET = 'your_client_secret' # replace with your client secret

# Replace with your playlist ID
PLAYLIST_ID = 'your_playlist_id' # Update with your actual playlist ID

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Function to fetch playlist tracks
def get_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    
    while results:
        for item in results["items"]:
            track = item["track"]
            if track:  # Ensure track is not None
                track_name = track["name"]
                artist_name = ", ".join([artist["name"] for artist in track["artists"]])
                tracks.append([track_name, artist_name])

        # Get next batch of songs (pagination)
        results = sp.next(results) if results["next"] else None

    return tracks

# Fetch tracks
tracks = get_playlist_tracks(PLAYLIST_ID)

# Save to CSV
df = pd.DataFrame(tracks, columns=["Song Title", "Artist"])
df = df.sort_values(by="Song Title")
df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"CSV file '{csv_filename}' has been created with {len(tracks)} songs.")
