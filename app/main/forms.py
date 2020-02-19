from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField("What is your interest?",validators=[Required()])
    category = RadioField('Label', choices=[ ('business','business'), ('love','love'),('medical','medical'),('motivational','motivational')],validators=[Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you' ,validators = [Required()] )
    submit = SubmitField('Submit')

