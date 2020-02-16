# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Smart Minute Pitch<h1>'

# if __name__=='__main__':
#     app.run(debug = True)

from app import app

if __name__ == '__main__':
    app.run()