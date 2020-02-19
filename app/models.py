from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255))
   email = db.Column(db.String(255),unique =True,index = True)
   role_id = db.Column(db.Integer)
   password_hash = db.Column(db.String(255))
   bio = db.Column(db.String(255))
   profile_pic_path = db.Column(db.String())
   pass_secure = db.Column(db.String(255))

   pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

   @property
   def password(self):
      raise AttributeError('You cannot read the password attribute')

   @password.setter
   def password(self, password):
      self.pass_secure = generate_password_hash(password)


   def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)
   
   def __repr__(self):
      return f'User {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    category = db.Column(db.String())
    
    writer = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        return pitches

    @classmethod
    def get_all_pitches(cls):
        pitches = Pitch.query.order_by('-id').all()
        return pitches


    def __repr__(self):
        return f'Pitch {self.pitch_title}'

class Review:

    all_reviews = []

    def __init__(self,pitch_id,title,review):
        self.pitch_id = pitch_id
        self.title = title
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()





class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.name}'