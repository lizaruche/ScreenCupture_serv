from app import app
from flask import send_from_directory, render_template
from main import STREAM
import os


@app.route('/favico.svg')
def favico():
    return send_from_directory(os.path.join(app.route_path, 'img/logo'), 'logo.svg')
