""" Models for Speakeasy app. """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

#this database defines the tables in an obj oriented way.
    #it outlines each table and the fields that exist for each

class User(db.Model): #one user has many bookings - one to many relationship
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    img = db.Column(db.String)

    bookings = db.relationship("Booking", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} fname={self.fname} lname ={self.lname}>'



#took syntax from rating in the movie ratings project in Hackbright demo's
class Booking(db.Model):
    """A booking."""

    __tablename__ = 'bookings'

    booking_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    arrival= db.Column(db.DateTime)
    departure = db.Column(db.DateTime)

    user = db.relationship("User", back_populates="bookings")
    location = db.relationship("Location", back_populates="bookings")

    def __repr__(self):
        return f'<Booking booking_id={self.booking_id} arrival={self.arrival} departure = {self.departure}>'

#many to many relationship between users a locations, middle table that has reviews in it.
#similar to locamen table below but with its own review attribute
class Review(db.Model):
    """A review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    body = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer) #should be 1-5

    location = db.relationship("Location", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")


    def __repr__(self):
        #this sets the format of my review obj
        return f"<Review id={self.review_id} title = {self.title} body ={self.body} score = {self.score}>"

class Location(db.Model): #one location has many amenity per location
    """A location."""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    location_title = db.Column(db.String)
    price = db.Column(db.Integer)
    overview = db.Column(db.String)
    description = db.Column(db.String)
    img = db.Column(db.String)

    images = db.relationship("Image", back_populates="location")
    bookings = db.relationship("Booking", back_populates="location")
    reviews = db.relationship("Review", back_populates="location")

    #relationship to amenities and location_amenties middle table
    amenities = db.relationship("Amenity", secondary = "location_amenities", back_populates = "locations")

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_title={self.location_title} price={self.price} amenities= {self.amenities}>'

class Image(db.Model): #many images for one location - many to one relationship
    """A image."""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    img_src = db.Column(db.String)
    img_tag = db.Column(db.String)

    #set up relationship to locations and image table
    location = db.relationship("Location", back_populates="images")

    def __repr__(self):
        return f'<Image image_id={self.image_id} img_src={self.img_src}>'


class Amenity(db.Model): #one amenity is related to a location with many amenities - one to many relationship
    """An amenity."""

    __tablename__ = 'amenities'

    amenity_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    amenity_title = db.Column(db.String)

    #set up relationship to locations and location_amenties middle table
    locations = db.relationship("Location", secondary = "location_amenities", back_populates = "amenities")

    def __repr__(self):
        return f'<Amenity amenity_id={self.amenity_id} amenity_title={self.amenity_title}>'



#took syntax from BookGenre in many to many demo
class LocationAmenity(db.Model): #middle table - do not need to save additional info here
    """An amenity in a specific location."""

    __tablename__ = "location_amenities"

    location_amenity_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"), nullable=False)
    amenity_id = db.Column(db.Integer, db.ForeignKey("amenities.amenity_id"), nullable=False)

    def __repr__(self):
        return f"<LocationAmenity location_id={self.location_id} amenity_id={self.amenity_id}>"



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



#dunder main statement
if __name__ == "__main__":
    import os

    #need to change text here
    os.system("dropdb projectdb --if-exists")
    os.system("createdb projectdb")

    connect_to_db(app)

    # Make our tables
    db.create_all()