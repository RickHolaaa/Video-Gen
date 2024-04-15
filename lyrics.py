from lyricsgenius import Genius
import lyricsgenius
import os
import string

import json

f = open('config.json')
data = json.load(f)
f.close()

class Lyrics:
    def __init__(self):
        """
            Init Genius instance
        """
        self.genius = Genius(data['client_access_token'], skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

    def get_lyrics(self, artist, title):
        """
            Retrive song's lyrics
        """
        artist = self.genius.search_artist(artist.split(",")[0],max_songs=0,sort="popularity")
        song = artist.song(title)

        lyrics = song.lyrics
        lyrics = "\n".join(lyrics.split("\n")[1:])
        lyrics = lyrics.split("Embed")[0].rstrip(string.digits)
        return lyrics


    def write_lyrics(self, artist, title, path):
        """
            Write lyrics in a file
        """
        lyrics = self.get_lyrics(artist.split(",")[0], title)
        f = open(path,"w")
        f.write(lyrics)
        f.close()

#print(lyrics("Taylor Swift","Enchanted"))
#print("\n".join(lyrics_to_string("Dua Lipa"," Dance The Night ").split("\n")[10:15]))
#write_lyrics("Dua Lipa"," Dance The Night ","dualipa.txt")

Rick = Lyrics()
print(Rick.get_lyrics('Taylor Swift', 'Enchanted'))
print(Rick.write_lyrics('Taylor Swift', 'Enchanted', 'toto.txt'))
