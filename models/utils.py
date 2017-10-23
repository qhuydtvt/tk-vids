from urllib.request import urlopen
import json


def load_web_json(path):
    with urlopen(path) as response:
        return json.loads(response.read().decode('utf-8'))


if __name__ == "__main__":
    topsong = load_web_json("https://itunes.apple.com/us/rss/topsongs/limit=50/genre=29/explicit=true/json")
    print(json.dumps(topsong, indent=4))
