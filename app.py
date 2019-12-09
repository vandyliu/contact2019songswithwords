import os
import sys
import pprint
import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
from dotenv import load_dotenv

USERNAME = os.getenv("USERNAME")

EDM_WITH_WORDS_PLAYLISTS = {
    '3O17naNo6YpCbGgSbuCBte',
    '38W9rZYlgIcprLZpId80ar',
    '62mIbOjQJrgbMTEdsNKPo1',
    '7Jl0KHDkICrLWUfRa7SIvq',
    '0AJrXIqOn6vXC2U9SG4cWq',
    "2YzLVDeUow7YOnwt7YiebS",
    "4u8aohKaKtXnCLp1u1is4I",
    "7GOzSS2YpabC4ChkCVKIuE",
    "3YtWGgbyZIZsq5oy7OsqGH",
    "6h67hkmJEMClpWxQVMrk6g",
    "2rBQG3P93sSOrIdDxws7GT",
    "14G2rYZNrlTggGEK0VTxYT",
    "5AUXqL32oa9eSK1L8qK4Rt",
    "4qZKd51eqNemzG2nS8lKnL",
    "5pXxecGjGSppPZGQN7vF7R",
    "5h1VjSm3bGaMCTAhUIWcQZ",
    "479FYLRAPD7LFuyuDW2qlp",
    "04Qc3DGB4nJ67PIel6p0hu",
    "3e0jJDD7paNSOQ4Fj1v3HS",
    "3O17naNo6YpCbGgSbuCBte",
    "1ZLyRPhekF5TGNZRqUULwj",
    "6u8mJ6grY4WfqhSCskl9TT",
    "2acs9BEzEM1RsRC6Ny06cI",
    "18Zu9lUVlpuFmcrYxztdvz",
    "6v5yLFt2sg0Nn4qUJNeDgY",
    "34ZiUhqnXHNPBGuqO5KWIn",
    "1vK5ZOq1njj2vu5gXNPp6z",
    "05HNvh3CkJ1bI8g5kqV2wq",
    "58LePg4kjZ3hirrj3z92Ka",
    "2uRWJrpzsYJWJu6swH57zU",
    "1Xnd8upSXvFDzlw1JhS872",
    "73MlSl1DVeiI7zTsoqHOzo",
    "4TaJfwDElxXeOtEdC5FR63",
    "3w21xLM1naAOEHggg7NCnI"
}

CONTACT_2019_PLAYLIST = '65HyKfAUIhAQn4ijSCo9l1'

CONTACT_2019_ARTISTS = {
    # day1
    "major_lazer": "738wLrAtLtCtFOLvQBXOXp",
    "kaskade": "6TQj5BFPooTa08A7pk8AQ1",
    "san_holo": "0jNDKefhfSbLR9sFvcPLHo",
    "droeloe": "0u18Cq5stIQLUoIaULzDmA",
    "g_jones": "0gXx2aQ2mfovDfqCw10MQC",
    "graves": "4E69riquObrTmBTVuF1b7B",
    "kompany": "7dtX3ykcuyVmts2HQnWgSP",
    "nittigritti": "21AUdblPrTRzkvJn8FGrlk",
    "said_the_sky": "4LZ4De2MoO3lP6QaNCfvcu",
    "tails": "007nYTXRhZJUZGH7ct5Y3v",
    "nostalgix": "6CarTAUaWnQb6bp7yjP0Zz",
    # day2
    "tiesto": "2o5jDhtHVPhrJdv3cEQ99Z",
    "rezz": "4aKdmOXdUKX07HVd3sGgzw",
    "fisher": "1VJ0briNOlXRtJUAzoUJdt",
    "bonnie_x_clyde": "74xeHqz5Ap8ZHq69TkxI0r",
    "dabin": "7lZauDnRoAC3kmaYae2opv",
    "destructo": "0BEYTctVmnYa5yStp4Jpab",
    "feed_me": "5FWi1mowu6uiU2ZHwr1rby",
    "wooli": "1Uyqa2sdHm1bL5JK4IC4zc",
    "wuki": "6Se1y4vDcu9fVHLqdj1N3q",
    "young_bombs": "4LKB1IkCINDDjEX8iS7glI",
    "sivz": "0NUhITSw1R757ncPIm3pGq",
    # not contact
    "audien": "4xnMDfgEmXZEEDdITKcGuE",
}

def setup():
    scope = 'playlist-modify-public'

    load_dotenv()
    auth = oauth2.SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
    )
    pretty_print = pprint.PrettyPrinter(indent=4)
    token = util.prompt_for_user_token(USERNAME, scope, client_id=os.getenv("SPOTIPY_CLIENT_ID"), client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
    sp = spotipy.Spotify(auth=token)
    return (pretty_print, sp)

def get_artists_in_playlist(playlist_id):
    playlist = sp.user_playlist(USERNAME, playlist_id=playlist_id)
    good_artists = set()
    for song in playlist["tracks"]["items"]:
        id = song["track"]["id"]
        artists = [artist["id"] for artist in song["track"]["artists"]]
        good_artists.update(artists)
    return good_artists

def get_songs_in_playlist(playlist_id, wanted_artists=None):
    playlist = sp.user_playlist(USERNAME, playlist_id=playlist_id)
    songs = set()
    for song in playlist["tracks"]["items"]:
        id = song["track"]["id"]
        artists = [artist["id"] for artist in song["track"]["artists"]]
        if wanted_artists == None or any(artist in wanted_artists for artist in artists):
            songs.add(id)
    return songs

def create_playlist_with_songs(name, songs):
    sp.user_playlist_create(USERNAME, name)
    # need to get id...
    sp.user_playlist_add_tracks(USERNAME, playlist_id='', track_ids=songs)

pp, sp = setup()
artist_ids = CONTACT_2019_ARTISTS.values()
pp.pprint(artist_ids)
songs = set()
for playlist in EDM_WITH_WORDS_PLAYLISTS:
    playlist_songs = get_songs_in_playlist(playlist, artist_ids)
    songs.update(playlist_songs)
list_of_songs = list(songs)
first_100_songs = list_of_songs[0:100]
last_songs = list_of_songs[100:]
sp.user_playlist_add_tracks(USERNAME, '1y29MKgZofWsYflp1LgkOd', first_100_songs)
sp.user_playlist_add_tracks(USERNAME, '1y29MKgZofWsYflp1LgkOd', last_songs)

# Find artists playing at contact --> Go through EDM songs and if an artist appears add it to playlist