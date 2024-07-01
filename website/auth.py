from flask import Blueprint, render_template, request, flash


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p> Log out </p>"

@auth.route("/sign-up", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        pass1 = request.form.get("password1")
        pass2 = request.form.get("password1")

        ##Sign up account information checks
        if len(email) < 4 or "@" not in email:
            flash("Email must be greater than 4 characters and contain the @ symbol", category = "error")
        elif pass1 != pass2:
            flash("Passwords do not match, please try again", category = "error")
        elif len(pass1) < 7:
            flash("Password cannot be less than 7 characters", category = "error")
        else:
            flash("Account created successfully!", category = "success")
    return render_template("sign_up.html")
