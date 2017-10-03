from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "How to use"


@app.route('/api/music')
def index():
    return "Music"

if __name__ == '__main__':
  app.run(debug=True)
