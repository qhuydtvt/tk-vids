from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import json

def get_vid_info(search_terms):
    ydl_options = {
        'format': 'bestaudio/best',
        'username': 'huynq.public',
        'password': 'hithere1989'
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(
                 "ytsearch1:{0}".format(search_terms),
                 download=False)
        return info


if __name__ == "__main__":
    info = get_vid_info("wake+me+up")
    print(json.dumps(info, indent=4))
