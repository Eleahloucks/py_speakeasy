"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
##run seed database when i make changes to model or crud to make sure they are working
# import cloudinary.uploader
import os

# CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
# CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
# CLOUD_NAME = 'doqa1yq0d'


from crud import *
connect_to_db(server.app)
db.drop_all()
db.create_all()



#SAMPLE USERS

user_1 = create_user('user1@email.com', "1234", "Michael", "Scott", "https://res.cloudinary.com/doqa1yq0d/image/upload/v1665002917/ifibmz147k74oi5jcku5.jpg")
user_2 = create_user('user2@email.com', "5678", "Pam", "Beasley",  "https://openpsychometrics.org/tests/characters/test-resources/pics/TO/4.jpg")
user_3 = create_user('user3@email.com', "9101112", "Dwight", "Schrutte",  "https://costumerocket.com/wp-content/uploads/Dwight-Schrute-shirt-.jpg")

print(user_1)
print(user_2)
print(user_3)

# user_check_1 = get_user_by_email('user1@email.com')
# user_check_2 = get_user_by_email('user2@email.com')
# user_check_3 = get_user_by_email('user3@email.com')

# print(user_check_1)
# print(user_check_2)
# print(user_check_3)




#SAMPLE LOCATIONS


# location_1 = create_location(
#   'Boulder, CO',
#   1869,
#   "Classic Craftsman in Colorado.",
#   "Made for a cozy mountain getaway, Boulder University Hill maintains its original wooden banister, fireplaces, and wooden floorboards. It has a wine cellar downstairs, and its large back deck is perfect for relaxing with your housemates. The neighborhood is known for its hilly roads, Victorian houses, and its close proximity to UC Boulder. It's a very bikeable area, and just minutes from the Boulder Farmer's Market or Pearl Street, where you'll find great restaurants, cafes, and shopping. Outsite Boulder - University Hill is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/boulder.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_10, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20]
#   )
# location_2 = create_location(
#   "Lisbon, Portugal",
#   1365,
#   "Comfortable coliving inside a historic building.",
#   "Outsite Lisbon is a traditional Lisbon building,- you’ll recognize it from it’s blue and white azulejos on the outside from Rua Sao Paulo. Pick a sea view on the south facing side of the building, or select a room with a balcony for the ultimate people-watching perch. There are 25 rooms in total, with a shared kitchen facility between every 5 rooms, and a large coworking space on the ground floor. Outsite Lisbon - Cais do Sodre is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/lisbon.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_3 = create_location(
#   'San Francisco, CA',
#   2968,
#   "A modern San Francisco home on California Street.",
#   "Make yourself at home in this four-floor house in Pacific Heights, San Francisco. There are 9 private bedrooms total, 6 of which have a shared bathroom, and 3 of which have their own en-suite. There's a backyard for summer barbecues, a modern, fully equipped kitchen and workspace in-house. Outsite San Francisco - Pacific Heights is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/sanfrancisco.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_4 = create_location(
#   'Manhattan, NY',
#   3003,
#   "Beautiful 5-story brownstone made for city living.",
#   "This is the spot for posting-up in New York - this traditional brownstone has a lounge room, fully equipped kitchen and large windows to let as much light in as possible. Work from the space, and head to one of Manhattan's coffee shops for a day's work. Outsite New York - Manhattan Midtown is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/manhattan.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_5 = create_location(
#   'Puerto Rico, San Juan',
#   1491,
#   "Airy, Spanish Style Home on the Beach.",
#   "Outsite Puerto Rico is your invite into island life. This ocean view home has plenty of outdoor space for making the most of San Juan's temperate climate, including a rooftop terrace. Hang out in the newly renovated kitchen when dining with friends, or explore the bay from your front doorstep. This space has beach access, so you can wake up and hit the water all before your morning calls. Outsite Puerto Rico - Ocean Park is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/puerto_rico.jpg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_6 = create_location(
#   'Morocco, North Africa',
#   1052,
#   "Restored Berber riad in the centre of Marrakesh.",
#   "A traditional riad complete with pool, hammam and rooftop terrace. Make use of the shared kitchen, indoor patios, outdoor terraces and the workspace, all furnished with ornate Moroccan textiles and crafts.  Outsite Marrakesh is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/morocco.jpg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_7 = create_location(
#   'Bidart, France',
#   1535,
#   "A traditional French country house, overlooking the Pyrenees.",
#   "This is a dreamy French country house dating back to 1870, finished with traditional tiles and stone interiors. There are 7 bedrooms, a kitchen, lounge and indoor pool, spread out between 2 floors. Private rooms are available with private and shared bathrooms. There's a heated pool on the ground floor, a tennis court, and an outdoor area for lounging in the sun - or setting up an enviable Zoom background. You'll have access to the tennis rackets, balls and e-bikes on-site for exploring during your stay. Outsite Bidart is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/france.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_8 = create_location(
#   'Canggu, Bali',
#   1407,
#   "Open, spacious villa with jungle views.",
#   "This is a true Balinese paradise, surrounded by palm trees and rice terraces. The garden and pool area sit at the center of the complex - the perfect outdoor place to workout, relax, or throw a get-together. When the heat gets too much, there's an air conditioned workspace, and shared kitchen for family dinners. There's an additional outdoor shelter for organising sound baths, meditations and massages too. Outsite Bali - Pererenan is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/bali.jpg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_9 = create_location(
#   'Fuerteventura, Canary Islands',
#   1240,
#   "An open plan space, designed to bring the outdoors in.",
#   "Wake up to volcano views and a dip in the pool in Outsite Canary Islands. This space is shouldered by 2 dormant volcanoes, and you can reach major surf beaches in 15 minutes drive. All rooms face an open, decked pool area, peppered with palm trees and native plants. Use the lounge or desk in your room for a few hours of focus, or meditate in the designated yoga room on-site. Outsite Canary Islands is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/canary_islands.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )
# location_10 = create_location(
#   'Santa Teresa, Costa Rica',
#   1375,
#   "Quality workspace meets ocean views in Costa Rica.",
#   "Nestled in the middle of Costa Rica's blue zone is Outsite Santa Teresa, a jungle villa. There are plenty of communal spaces to work from and unwind in, all of which are open-air and offer panoramic views of the Pacific. Sunsets are magical here - opt to watch them from the living room, or from your own private terrace. The house is in a gated community at the top of a hill. You'll find a pool just before the gate to cool off in on your way into town. Outsite Santa Teresa is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
#   "/static/img/costa_rica.jpeg",
#   [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
#   )




# check_1 = get_location_by_id(1)
# check_2 = get_location_by_id(2)
# check_3 = get_location_by_id(3)

# print(check_1)
# print(check_2)
# print(check_3)



#REVIEW DATA
# def create_review(title, body, score, user_id, location_id):



# review_1 = create_review(title = "Amazing stay!", body = "I was so happy to spend a full two months at the Outsite house in North Boulder! ful roommates during my stay - I felt so lucky! Don't hesitate to spend time her if you love the outdoors and nature", score = 5, user_id = 1, location_id = 1)
# review_2 = create_review("Great and affordable to remote work and meet others!", "Outsite was truly a great experience. The WhatsApp group was an easy way to connect with others traveling/working in Lisbon. The accommodations are clean and kept up nicely by staff and others staying", 5, 2, 2)
# review_3 = create_review("The Location, the people and the kitchen!","My stay in San Francisco was great. The house is large and in a perfect Pac heights location. It's very walkable with lots of restaurants, parks and studios near by. There was ample space to work and the kitchen was great to cook in!", 4, 3, 3 )
# review_4 = create_review(title = "Amazing stay!", body = "I was so happy to spend a full two months at the Outsite house in North Boulder! ful roommates during my stay - I felt so lucky! Don't hesitate to spend time her if you love the outdoors and nature", score = 5, user_id = 1, location_id = 4)
# review_5 = create_review("Great and affordable to remote work and meet others!", "Outsite was truly a great experience. The WhatsApp group was an easy way to connect with others traveling/working in Lisbon. The accommodations are clean and kept up nicely by staff and others staying", 5, 2, 5)
# review_6= create_review("The Location, the people and the kitchen!","My stay in San Francisco was great. The house is large and in a perfect Pac heights location. It's very walkable with lots of restaurants, parks and studios near by. There was ample space to work and the kitchen was great to cook in!", 4, 3, 6 )
# review_7 = create_review(title = "Amazing stay!", body = "I was so happy to spend a full two months at the Outsite house in North Boulder! ful roommates during my stay - I felt so lucky! Don't hesitate to spend time her if you love the outdoors and nature", score = 5, user_id = 1, location_id = 7)
# review_8 = create_review("Great and affordable to remote work and meet others!", "Outsite was truly a great experience. The WhatsApp group was an easy way to connect with others traveling/working in Lisbon. The accommodations are clean and kept up nicely by staff and others staying", 5, 2, 8)
# review_9 = create_review("The Location, the people and the kitchen!","My stay in San Francisco was great. The house is large and in a perfect Pac heights location. It's very walkable with lots of restaurants, parks and studios near by. There was ample space to work and the kitchen was great to cook in!", 4, 3, 9 )
# review_10 = create_review("The Location, the people and the kitchen!","My stay in San Francisco was great. The house is large and in a perfect Pac heights location. It's very walkable with lots of restaurants, parks and studios near by. There was ample space to work and the kitchen was great to cook in!", 4, 3, 10 )
# review_5 = create_review("Great and affordable to remote work and meet others!", "Outsite was truly a great experience. The WhatsApp group was an easy way to connect with others traveling/working in Lisbon. The accommodations are clean and kept up nicely by staff and others staying", 5, 2, 8)





# review_check_1 = get_review_by_location_id(1)
# review_check_2 = get_review_by_user_id(2)
# review_check_3 = get_review_by_location_id(3)
# review_check_1 = get_review_by_location_id(4)
# review_check_2 = get_review_by_user_id(5)
# review_check_3 = get_review_by_location_id(6)
# review_check_1 = get_review_by_location_id(7)
# review_check_2 = get_review_by_user_id(8)
# review_check_3 = get_review_by_location_id(9)
# review_check_1 = get_review_by_location_id(10)

# print(review_1)
# print(review_2)
# print(review_3)
# print(review_4)
# print(review_5)
# print(review_6)
# print(review_7)
# print(review_8)
# print(review_9)
# print(review_10)




#IMAGES DATA

#implent cloudinary
# cloudinary.config(
#   cloud_name = CLOUD_NAME,
#   api_key = CLOUDINARY_KEY,
#   api_secret = CLOUDINARY_SECRET,
#   secure = True
# )


#write a function grab img by tag returns an array of img info by tag - seed
# def grab_img_by_tag(img_tag):
#   """create a gallery with a list of img urls by tag"""
#   gallery = []
#   tag_json_obj = cloudinary.Search().expression(f'tags=#{img_tag}').execute()
#   # print(tag_json_obj)
#   img_one = tag_json_obj['resources'][0]['secure_url']
#   img_two = tag_json_obj['resources'][1]['secure_url']
#   img_three = tag_json_obj['resources'][2]['secure_url']
#   img_four = tag_json_obj['resources'][3]['secure_url']
#   img_five = tag_json_obj['resources'][4]['secure_url']



