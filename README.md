# Import (an Excel) song list into a Spotify playlist
March 2025

I was given a list of 434 songs and wanted to create a corresponding Spotify playlist, but the only existing solutions were by a third-party and I didn't want to allow access to my personal Spotify credentials. Instead, here is a Python script I developed to take a list of songs in CSV format (expects columns "Song" and "Artist") and add them to a Spotify playlist.
```
import_CSV_to_spotify.py
```

Also provided is a Python script to generate a CSV with the list of songs from a Spotify playlist.
```
list_songs_in_playlist.py
```

## Instructions for use
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/) and create an app (use `http://localhost:8888/callback` for redirect URI).
2. Get your API credentials (Client ID and Client Secret)
3. Install Spotipy and pandas: Run `pip install spotipy pandas` if you haven’t already (or `pip install -r requirements.txt` with the provided file in this repo).
4. Run the script, providing your playlist ID, Client ID, and Client secret.

## Additional info

- The `playlist ID` can be found in the playlist URL, which you can find by clicking on `Share > Copy link to playlist` when viewing the playlist in Spotify, and pasting it into your choice of text editor. Note that the project ID is around 22 alphanumeric characters (my playlist URL showed as: `https://open.spotify.com/playlist/0AF3HmVvQqGkjXrCHjqIkU?si=ytkXbRF5RYeeKFHaE62Obg&pi=k0aZBroxT7SrT` but the project ID is `0AF3HmVvQqGkjXrCHjqIkU`).

- The playlist can be empty or can have contents.

- The script will print a `SONG NOT FOUND` message if can't find the corresponding song on Spotify.

- a demo CSV is provided: `song_test.csv`