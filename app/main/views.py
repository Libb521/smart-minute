from flask import render_template,request,redirect,url_for,abort
# from app import app
# from ..models import Review
from .forms import ReviewForm, UpdateProfile
from flask_login import login_required, login_user
from ..models import User
from .. import db
from . import main

#views
@main.route('/')
def index():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Smart Minute Pitch'
   message = 'SMART MINUTE PITCH'
   return render_template('index.html', message = message, title = title)

@main.route('/')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/love/pitches/')
# @login_required
def love():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Smart Minute Pitch'  
    return render_template('love.html', title = title )

@main.route('/motivational/pitches/')
# @login_required
def motivational():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Smart Minute Pitch'  
    return render_template('motivational.html', title = title )

@main.route('/business/pitches/')
# @login_required
def business():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Smart Minute Pitch'  
    return render_template('business.html', title = title )
   
@main.route('/medical/pitches/')
# @login_required
def medical():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Smart Minute Pitch'  
    return render_template('medical.html', title = title )

@main.route('/pitch/<int:id>')
def pitch(id):
    
    reviews = Review.get_reviews(pitch_id)
    return render_template('pitch.html',id = pitch_id, reviews=reviews)


@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(pitch.id,title,review)
        new_review.save_review()
        return redirect(url_for('main.index' ))

    title = f'{pitch.title} review'
    return render_template('new_review.html',id = pitch_id,title = title, review_form=form, pitch=pitch)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

import urllib.request,json
# from .models import get_pitches

def get_pitches(category):
    '''
    Function that gets the json response to our url request
    '''
    get_pitches_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_pitches_data = url.read()
        get_pitches_response = json.loads(get_pitches_data)

        pitch_results = None

        if get_pitches_response['results']:
            pitch_results_list = get_pitches_response['results']
            pitch_results = process_results(pitch_results_list)


    return pitch_results

def process_results(pitch_list):
  
    pitch_results = []
    for pitch_item in pitch_list:
        id = pitch_item.get('id')
        title = pitch_item.get('original_title')

        if pitch:
            pitch_object = pitch(id,title)
            pitch_results.append(pitch_object)

    return pitch_results