from flask import Blueprint, render_template

#Define view.py as a blueprint for the site: contains a number of roots/URLs inside

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")

@views.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@views.route("/login")
def login():
    return render_template("login.html")




