from youtube import get_vid_info
from nhaccuatui import get_song_source


def get_music_info(search_terms):
    entries = get_vid_info(search_terms)["entries"]
    if len(entries) == 0:
        return None
    vid_info = entries[0]
    url = get_song_source(search_terms)
    return {
        'thumbnail': vid_info['thumbnail'],
        'url': url
    }
