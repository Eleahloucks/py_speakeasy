"""CRUD operations."""
#CRUD - created helper functions that manage operations of create read update and delete. Doesnt have to be named crud.

from model import db, User, Location, Review, connect_to_db
from datetime import datetime



#MVP - speakeasy app
  # Use Google Maps API & cloudninary

#TO DO
#connect api's
#add seed data for recipe's and location



#USER FUNCTIONS
def create_user(email, password, fname, lname, img):
    """Create and return a new user."""

    user = User(email=email, password=password, fname = fname, lname = lname, img = img)
    db.session.add(user)
    db.session.commit()

    return user

def get_all_users():
    """Return a list of all users in the database."""

    return User.query.all()

def get_user_by_email(email):
    """Return user by looking up their email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return user by looking up their id."""

    return User.query.get(user_id)


#REVIEW FUNCTIONS
# def create_review(title, body, score, user_id, location_id):
#   """Create a review."""

#   review = Review(title = title, body = body, score = score, user_id = user_id, location_id = location_id)
#   db.session.add(review)
#   db.session.commit()

#   return review

# def get_review_by_location_id(location_id):
#     """Get review by location id."""

#     return Review.query.filter(Review.location_id == location_id).first()

# def get_review_by_user_id(user_id):
#     """Get review by user id."""

#     return Review.query.filter(Review.user_id == user_id).first()


#LOCATION FUNCTIONS
# def get_all_locations():
#     """Return a list of all locations in the database."""

#     return Location.query.all()

# def create_location(location_title, price, overview, description, img, amenities):
#   """Create a location instance."""

#   location = Location(location_title = location_title, price = price, overview = overview, description = description, img = img, amenities = amenities)
#   db.session.add(location)
#   db.session.commit()

#   return location

# def get_location_by_id(location_id):
#   """Get location by id."""

#   return Location.query.get(location_id)


#IMAGE FUNCTIONS
# def create_image(location_id, img_src, img_tag):
#   """Create a image instance."""

#   image = Image(location_id = location_id, img_src = img_src, img_tag = img_tag)
#   db.session.add(image)
#   db.session.commit()

#   return image




#dunder name dunder main syntax from crud in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
