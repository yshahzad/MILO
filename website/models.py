from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Each set is connected to a user and an exercise
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    exercise = db.Column(db.String, db.ForeignKey("exercise"))


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Each exercise is connected to a user and a workout
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    exercise = db.Column(db.String, db.ForeignKey("workout"))


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class StrengthWorkout(db.Model, Workout):
    pass


class CardioWorkout(db.Model):
    pass


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10_000))
    date = db.Column(db.DateTime(timezone=True), default = func.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #A foreign key is a column in a database that references a column in another table,
    #used to link together classes. Here, you must pass an existing user_id to create a note.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # A unique identifier for the object
    email = db.Column(db.String(150), unique=True)  # unique = True => no two users can have the same email
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship("Note")
