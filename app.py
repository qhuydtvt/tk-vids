from flask import Flask, render_template, request, url_for
from youtube import get_vid_info
from flask_restful import Resource, Api
from os.path import join
from urllib.request import urlopen
import json
import mlab
from models.audio import Audio
app = Flask(__name__)

mlab.connect()

def webpage_str(url):
    return urlopen(url).read.decode('utf-8')

not_found_message = json.dumps ({
    "sucess": 0,
    "data": "not_found"
})



@app.route('/')
def index():
    # open(join(app.root_path, "/data/music_result.txt")).read().decode('utf-8')
    music_result = open(join(app.root_path, "data", "music_result.txt")).read()
    guide_list = [
        {
            "title": "Pure audio search",
            "example": url_for("audio_search") + "?search_terms=wake+me+up+acivii",
            "format": url_for("audio_search") + "?search_terms=<Enter song|artist here>"
        }
    ]
    return render_template("index.html", guide_list=guide_list)


@app.route('/api/audio')
def audio_search():
    search_terms = request.args["search_terms"]

    vid_info = get_vid_info(search_terms)
    if  "entries" not in vid_info:
        return not_found_message
    elif len(vid_info["entries"]) == 0:
        return not_found_message
    else:
        if "formats" in vid_info["entries"][0]:
            del vid_info["entries"][0]["formats"]
        entry = vid_info["entries"][0]



        return json.dumps({
            "sucess": 1,
            "data": {
                "url": entry["url"],
                "thumbnail": entry["thumbnail"],
                "description": entry["description"]
            }}, indent=4)


if __name__ == '__main__':
  app.run(debug=True)
