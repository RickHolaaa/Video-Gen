import requests
import pandas as pd
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

f = open('config.json')
data = json.load(f)
f.close()
client_id = data['client_id']
client_secret = data['client_secret']
redirect_uri = 'http://127.0.0.1:9090'
scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirect_uri,
                                           scope=scope))
class SpotifyClass:
    def __init__(self):
        """
            Get Top 50 Best songs on Spotify
        """
        """
        First version
        self.url = 'https://charts-spotify-com-service.spotify.com/public/v0/charts'
        response = requests.get(self.url)
        self.chart = []
        for entry in response.json()['chartEntryViewResponses'][0]['entries']:
            self.chart.append({
                "Rank": entry['chartEntryData']['currentRank'],
                "Artist": ', '.join([artist['name'] for artist in entry['trackMetadata']['artists']]),
                "TrackName": entry['trackMetadata']['trackName']
            })
        """
        self.chart = self.get_tracks_from_album()
    def get_top_nth(self, n=10):
        """
            Get nth first best songs on Spotify
        """
        return pd.DataFrame(self.chart[0:n])

    def get_tracks_from_album(self, url = 'https://open.spotify.com/album/5j0o3XQ1YciVzm7MtcFmfG?si=bIC7r7FmTwa0-7EA0LyyCg'):
        """
            Get tracks from album
        """
        uri = url.split('?si')[0].split('/')[-1]
        results = sp.album_tracks(uri)
        chart = []
        for i in results['items']:
            chart.append({
                "Rank":i['track_number'],
                "Artist":i['artists'][0]['name'],
                "TrackName":i['name']
                })
        return chart

    def get_test(self, url = 'https://open.spotify.com/album/5j0o3XQ1YciVzm7MtcFmfG?si=GdBBLFQ5RX61HIhC7NVVUQ'):
        uri = url.split('?si')[0].split('/')[-1]
        results = sp.album_tracks(uri)
        chart = []
        for i in results['items']:
            chart.append({
                "Rank":i['track_number'],
                "Artist":i['artists'][0]['name'],
                "TrackName":i['name'],
                "PreviewUrl":i['preview_url']
                })
        return chart

Rick = SpotifyClass()
#print(Rick.get_top_nth(20))
#print(Rick.get_tracks_from_album())
