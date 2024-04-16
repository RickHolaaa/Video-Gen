from download import *

class Recap:
    def __init__(self):
        self.spot = SpotifyClass() 
    def generate_tracks(self, url = 'https://open.spotify.com/album/5j0o3XQ1YciVzm7MtcFmfG?si=GdBBLFQ5RX61HIhC7NVVUQ'):
        return self.spot.get_tracks_from_album(url)
    def generate_recap(self, url = 'https://open.spotify.com/album/5j0o3XQ1YciVzm7MtcFmfG?si=GdBBLFQ5RX61HIhC7NVVUQ'):
        results = self.spot.get_test(url)
        # Download preview
        for res in results:
            artist = res['Artist'].lower().replace(' ', '-')
            song = res['TrackName'].lower().replace(' ','-')
            path = './Songs/'
            with open(path+song+'-'+artist+'.mp3', 'wb') as sg:
                resp = requests.get(res['PreviewUrl'])
                if (resp.status_code == 200):
                    sg.write(resp.content)
                    print(f'{song} - {artist} was successfully installed in {path}')
                else:
                    print(f'Failed to download {song} - {artist}')
            

Rick = Recap()

Rick.generate_recap()
