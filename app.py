from flask import Flask, render_template, request, url_for
from music_dl import get_music_info
from flask_restful import Resource, Api
from os.path import join
from urllib.request import urlopen
from nhaccuatui import get_song_source
import json
import mlab
from models.audio import Audio
from flask_restful import Resource, Api
import models.utils

app = Flask(__name__)
api = Api(app)

mlab.connect()

class ApiAudio(Resource):
    def get(self):
        search_terms = request.args["search_terms"].lower().strip()

        audio = Audio.objects(search_terms=search_terms).first()

        if audio is not None:
            return {
                'success': 1,
                'data': mlab.item2json(audio)
            }
        else:
            return {
                'success': 0,
                'message': 'Not found'
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
    rule = request.url_rule
    guide_list = [
        {
            "title": "Pure audio search",
            "example": "api/audio?search_terms=thunder+imagine+dragons",
            "format": "api/audio?search_terms=<Enter song|artist here>",
            "parse_xml": "http://bit.ly/tk-xml-parser"
        }
    ]
    return render_template("index.html", guide_list=guide_list)

api.add_resource(ApiAudio, '/api/audio')

if __name__ == '__main__':
    app.run(port=1212)
