# """Models for speakeasy app."""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
""" Models for Innsite app. """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

#this database defines the tables in an obj oriented way.
    #it outlines each table and the fields that exist for each



class User(db.Model): #one user can upload many recipies, reviews and locations- one to many relationship
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    # location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    # review_id = db.Column(db.Integer, db.ForeignKey("reviews.review_id"))
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    img = db.Column(db.String)

    #user is singular because each location, review and recipe have one user
    locations = db.relationship("Location", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    recipes = db.relationship("Recipe", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} fname={self.fname} lname ={self.lname}>'

#each review has one user(many to one)
#each review occurs at only one location(many to one)
class Review(db.Model):
    """A review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    body = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer) #should be 1-5

    #reviews is plural bc of many to one
    location = db.relationship("Location", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")


    def __repr__(self):
        #this sets the format of my review obj
        return f"<Review id={self.review_id} title = {self.title} body ={self.body} score = {self.score}>"

class Location(db.Model): #one location has many reviews and users(many to one)
    """A location."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    # review_id = db.Column(db.Integer, db.ForeignKey("reviews.review_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_title = db.Column(db.String)
    price = db.Column(db.Integer)
    overview = db.Column(db.String)
    description = db.Column(db.String)
    img = db.Column(db.String)

    reviews = db.relationship("Review", back_populates="location")
    user = db.relationship("User", back_populates="locations")

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_title={self.location_title} price={self.price}>'

class Recipe(db.Model): #one recipe is related to a user that could have uploaded many recipies - many to one relationship
    """A recipe."""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    recipe_title = db.Column(db.String)
    recipe_description = db.Column(db.String)
    recipe_specs = db.Column(db.String)

    user = db.relationship("User", back_populates = "recipes")

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} recipe_title={self.recipe_title}>'


#connect to db took syntax from many to many lecture demo
def connect_to_db(app):
    """Connect to database."""

    #stating which db to connect to
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///projectdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # this would output the raw SQL, currently off as it can be noisy
    # app.config["SQLALCHEMY_ECHO"] = True

    db.app = app
    db.init_app(app)

    print("Connected to the db!")



#dunder main statement
if __name__ == "__main__":
    import os

    #need to change text here
    os.system("dropdb projectdb --if-exists")
    os.system("createdb projectdb")

    with app.app_context():
        connect_to_db(app)

        # Make our tables
        db.create_all()
