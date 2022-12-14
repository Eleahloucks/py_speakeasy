"""Server for work travel co-living app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
# from datetime import datetime
from model import connect_to_db, db
import crud
# import cloudinary.uploader
import os

# CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
# CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
# CLOUD_NAME = 'doqa1yq0d'

from jinja2 import StrictUndefined

#imports form model and crud
#responds to http requests, each route has a view function that may call for data from db and will either return a template or json
#some routes handle post requests

app = Flask(__name__)
app.secret_key = "dev" # fixme
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Show homepage"""
    all_locations = crud.get_all_locations()

    return render_template("homepage.html", locations = all_locations)

# @app.route("/locations")
# def show_all_locations():
#     """Show all locations"""
#     all_locations = crud.get_all_locations()
#     return render_template("all_locations.html", locations = all_locations)

# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")

# @app.route('/create-account', methods=["GET"])
# def show_create_account_form():
#     """Display about create account."""

#     return render_template("new_account.html")

# @app.route('/create-account', methods = ['POST'])
# def process_new_account():
#     """Create new account."""
#     fname = request.form.get('fname')
#     lname = request.form.get('lname')
#     email = request.form.get('email')
#     password = request.form.get('password')
#     photo= request.files['my-file']

#     cloudinary_request = cloudinary.uploader.upload(photo, cloud_name = CLOUD_NAME, api_key = CLOUDINARY_KEY, api_secret = CLOUDINARY_SECRET)
#     img = cloudinary_request['secure_url']

#     user = crud.create_user(email, password, fname, lname, img)

#     return redirect("/")
#     #psql to check

# @app.route("/login", methods = ['POST'])
# def process_login():
#     """Show login"""
#     input_email = request.form.get('email')
#     input_password = request.form.get('password')
#     #will retrieve a user obj or none.
#     potential_user = crud.get_user_by_email(input_email)
#     #if user is none
#     if not potential_user:
#         flash('user not found!')
#     #if user is found check pw
#     elif potential_user.password == input_password:
#         session['user_id'] = potential_user.user_id
#         session['email'] = potential_user.email
#         session['fname'] = potential_user.fname

#         return redirect("/")
#     #user was found but pw didnt match
#     else:
#         flash('Not logged in!')
#     return render_template("login.html")


# @app.route("/locations/<location_id>")
# def location_details(location_id):
#     """Show details of a location."""
#     location = crud.get_location_by_id(location_id)
#     reviews = crud.get_review_by_location_id(location_id)
#     return render_template("location_details.html", location = location, reviews = reviews)


# @app.route("/locations/<location_id>", methods = ['POST'])
# def book_location(location_id):
#     """book a location."""

#     arrival = request.json.get("arrival")
#     departure = request.json.get("departure")
#     booked_location = request.json.get("location")
#     location = crud.get_location_by_id(location_id)
#     # Figure out how to get the times to work.
#     user = crud.get_user_by_id(session['user_id'])
#     # crud.create_booking(arrival, departure, user, booked_location)
#     #or this format
#     booking = crud.create_booking(arrival = crud.get_datetime_format(arrival), departure = crud.get_datetime_format(departure), user= user, location = location)

#     return jsonify({
#         "sucess": True,
#         "status": f"Your booking from {crud.get_datetime_format(arrival)} to {crud.get_datetime_format(departure)} in {booked_location} is confirmed!"
#     })

# @app.route("/book-now", methods=["GET"])
# def show_book_now():
#     """Show booking page."""
#     all_locations = crud.get_all_locations()

#     return render_template("book_now.html", locations = all_locations)

# @app.route("/profile/")
# def show_profile():
#     """Show user profile."""
#     user = crud.get_user_by_id(session['user_id'])

#     return render_template("profile.html", user = user, crud = crud)

# @app.route("/sign-out", methods = ['POST'])
# def sign_out_user():
#     """Sign out user"""

#     session.clear()

#     return redirect("/")


# @app.route('/about')
# def show_about():
#     """Display about page."""

#     return render_template("about.html")

# @app.route('/new-review')
# def show_review_form():
#     """Display review form template."""
#     all_locations = crud.get_all_locations()
#     user = crud.get_user_by_id(session['user_id'])


#     return render_template("reviewform.html", all_locations = all_locations, user = user, crud = crud)


# @app.route("/new-review", methods = ['POST'])
# def new_review():
#     """Write a review."""
#     name = request.form.get("name")
#     email = request.form.get("email")
#     location = request.form.get("location")
#     rating = request.form.get("score")
#     title = request.form.get("title")
#     body = request.form.get("body")

#     flash("Thank you for your feedback!")

#     return redirect("/")

# @app.route('/test')
# def show_test():
#     """Display test page."""
#     all_locations = crud.get_all_locations()

#     return render_template("test.html", all_locations = all_locations)











#dunder main syntax from movie ratings server.py file
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)