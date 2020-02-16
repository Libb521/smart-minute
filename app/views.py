from flask import Flask, render_template
from app import app
# from ..request import get_pitches

#views
@app.route('/')
def index():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Smart Minute Pitch'
   message = 'SMART MINUTE PITCH'
   return render_template('index.html', message = message, title = title)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
   '''
   views pitches posted by other users
   '''

   return render_template('pitch.html',id = pitch_id)