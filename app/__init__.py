from flask import Flask, render_template
from .config import Configuration

app = Flask(__name__)

app.config.from_object(Configuration)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"
