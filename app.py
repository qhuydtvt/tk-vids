from flask import Flask, render_template, request, url_for
from youtube import get_vid_info
from flask_restful import Resource, Api
from os.path import join
from urllib.request import urlopen
import json
import mlab
from models.audio import Audio
from flask_apscheduler import APScheduler
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

mlab.connect()

class ApiAudio(Resource):
    def get(self):
        search_terms = request.args["search_terms"].lower()

        audio = Audio.objects(search_terms=search_terms).first()
        if audio is not None:
            return {
                'success': 1,
                'data': mlab.item2json(audio)
            }
        else:
            vid_info = get_vid_info(search_terms)
            if  "entries" not in vid_info:
                return not_found_message
            elif len(vid_info["entries"]) == 0:
                return not_found_message
            else:
                if "formats" in vid_info["entries"][0]:
                    del vid_info["entries"][0]["formats"]
                entry = vid_info["entries"][0]

                audio = Audio(search_terms=search_terms, url=entry["url"], thumbnail=entry["thumbnail"], description=entry["description"])
                audio.save()

                return {
                    'success': 1,
                    'data': mlab.item2json(audio)
                }



def webpage_str(url):
    return urlopen(url).read.decode('utf-8')

not_found_message = json.dumps ({
    "sucess": 0,
    "data": "not_found"
})


@app.route('/')
def index():
    music_result = open(join(app.root_path, "data", "music_result.txt")).read()
    guide_list = [
        {
            "title": "Pure audio search",
            "example": url_for("apiaudio") + "?search_terms=wake+me+up+acivii",
            "format": url_for("apiaudio") + "?search_terms=<Enter song|artist here>"
        }
    ]
    return render_template("index.html", guide_list=guide_list)

api.add_resource(ApiAudio, '/api/audio')

if __name__ == '__main__':
    app.run()
