import models.utils as utils
from models.audio import Audio
from models.subgenre import subgenres
from music_dl import get_music_info
from youtube_dl.utils import DownloadError

import json


def preload_songs():
    for subgenre in subgenres:
        preload_one_song(subgenre["id"])


def preload_one_song(genre_no):
    GENRE_URL_FORMAT = "https://itunes.apple.com/us/rss/topsongs/limit=50/genre={0}/explicit=true/json"
    genre_url = GENRE_URL_FORMAT.format(genre_no)
    genre_json = utils.load_web_json(genre_url)

    for entry in genre_json["feed"]["entry"]:
        search_terms = extract_search_terms(entry)
        print("Searching for", search_terms, "...")
        if not Audio.exists(search_terms):
            print("Search terms does not exists, extract and add into database")
            try:
                vid_info = get_music_info(search_terms)
                if vid_info is None:
                    print("Found no videos")
                else:
                    Audio.save_from_dict(search_terms, vid_info)
            except DownloadError:
                print("Download error")
        else:
            print("Search terms already exists")

def extract_search_terms(entry):
    name = entry["im:name"]["label"]
    artist = entry["im:artist"]["label"]
    return "{0} {1}".format(name.strip().lower(), artist.strip().lower())


if __name__ == "__main__":
    # print(json.dumps(preload_one_song(20), indent=4))
    import mlab
    mlab.connect()
    preload_songs()
