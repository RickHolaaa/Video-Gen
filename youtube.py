from youtubesearchpython import VideosSearch

def search(title,choices = 10):

    filtre = ['Remix', 'Live', 'Dubstep', '(Slowed Down)',
              'official music video', 'official video','Lyric Video']

    videosSearch = VideosSearch(title, limit = choices, region = 'FR')

    results = videosSearch.result()['result']

    filtered_videos = [res for res in results
                       if not any(exc.lower() in res['title'].lower() for exc
                                  in filtre)]

    print("avt:",results[0]['link'])
    print("apr:",filtered_videos[0]['link'])

    return filtered_videos[0]['link']
