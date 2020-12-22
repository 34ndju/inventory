import flask
from app import app

@app.route('/')
def home():
    return flask.render_template('analytics.html')

@app.route('/index')
def index():
    return flask.render_template('index.html')
