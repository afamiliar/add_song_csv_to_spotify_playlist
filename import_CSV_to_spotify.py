# Read in a CSV of songs and add them to an existing Spotify playlist
#   March 2025
#
#       inputs:
#           csv_file          incl. columns "Song", "Artist"
#           playlist_id       ID of Spotify playlist to add songs to

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time

# Spotify API credentials (set up an app at https://developer.spotify.com/)
CLIENT_ID = 'your_client_id' # update with your Client ID
CLIENT_SECRET = 'your_client_secret' # update with your Client Secret
REDIRECT_URI = 'http://localhost:8888/callback' # use this when creating the app
SCOPE = 'playlist-modify-public playlist-modify-private'

# Initialize Spotify client
def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

# Read CSV file (expects columns: 'Song' and 'Artist')
def read_songs_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return list(zip(df['Song'], df['Artist']))

# Search for song URIs
def get_song_uris(sp, songs):
    song_uris = []
    for song, artist in songs:
        query = f'track:{song} artist:{artist}'
        results = sp.search(q=query, type='track', limit=1)
        tracks = results.get('tracks', {}).get('items', [])
        if tracks:
            song_uris.append(tracks[0]['uri'])
        else:
            print(f'SONG NOT FOUND: {song} - {artist}')
        time.sleep(0.2)  # Avoid hitting API rate limits
    return song_uris

# Add songs to playlist
def add_songs_to_playlist(sp, playlist_id, song_uris):
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

if __name__ == '__main__':
    csv_file    = 'song_list.csv'  # Update with your actual CSV file
    playlist_id = 'your_playlist_id' # Update with your actual playlist ID

    sp = get_spotify_client()
    songs = read_songs_from_csv(csv_file)
    song_uris = get_song_uris(sp, songs)

    if song_uris:
        add_songs_to_playlist(sp, playlist_id, song_uris)
        print(f'Added {len(song_uris)} songs to the playlist!')
    else:
        print('No songs found to add.')
