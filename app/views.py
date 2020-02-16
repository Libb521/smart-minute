from flask import Flask, render_template
from app import app

#views
@app.route('/')
def index():

   '''
   View root page function that returns the index page and its data
   '''

   message = 'SMART MINUTE PITCH'
   return render_template('index.html', message = message)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
   '''
   views pitches posted by other users
   '''

   return render_template('pitch.html',id = pitch_id)