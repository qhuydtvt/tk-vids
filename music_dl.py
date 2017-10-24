from youtube import get_vid_info
from nhaccuatui import get_song_source


def get_music_info(search_terms):
    entries = get_vid_info(search_terms)["entries"]
    if len(entries) == 0:
        return None
    vid_info = entries[0]
    print("Getting song source: " + search_terms)
    url = get_song_source(search_terms)
    if url is None:
        return None
    return {
        'thumbnail': vid_info['thumbnail'],
        'url': url
    }

if __name__ == "__main__":
    print(get_music_info("dança do creu mc créu"))
