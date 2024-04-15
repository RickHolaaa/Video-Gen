import requests
import pandas as pd

class SpotifyClass:
    def __init__(self):
        """
            Get Top 50 Best songs on Spotify
        """
        self.url = 'https://charts-spotify-com-service.spotify.com/public/v0/charts'
        response = requests.get(self.url)
        self.chart = []
        for entry in response.json()['chartEntryViewResponses'][0]['entries']:
            self.chart.append({
                "Rank": entry['chartEntryData']['currentRank'],
                "Artist": ', '.join([artist['name'] for artist in entry['trackMetadata']['artists']]),
                "TrackName": entry['trackMetadata']['trackName']
            })

    def get_top_nth(self, n=10):
        """
            Get nth first best songs on Spotify
        """
        return pd.DataFrame(self.chart[0:n])

Rick = SpotifyClass()
print(Rick.get_top_nth(20))
