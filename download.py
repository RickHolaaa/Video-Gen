from pytube import YouTube
from youtube import *
from spotify import *
import os

Rick = SpotifyClass()

def download(rank):
    title = Rick.get_top_nth(rank)['TrackName'].tolist()[-1]
    artist = Rick.get_top_nth(rank)['Artist'].tolist()[-1]
    yt = YouTube(search(title+'-'+artist),use_oauth=False,allow_oauth_cache=True)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path="Songs")
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = "./Songs/"+title.replace(' ','-').lower()+'.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title+ " has been successfully downloaded.")
    return new_file,yt.title

[download(i) for i in range(1,20)]
