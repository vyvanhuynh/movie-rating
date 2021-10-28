""" Use this script to facilitate a database setup instead of manually 
    typing commands each time we have new data to seed the database """

import os, json
from random import choice, randint
from datetime import datetime
import crud, model, server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings  
movies_in_db = []
for data in movie_data:
    title = data["title"]
    release_date = datetime.strptime(data["release_date"],"%Y-%m-%d")
    poster_path = data["poster_path"]
    overview = data["overview"]

    # This db_movie is one row of the movie table 
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = f'test{n}'
    user = crud.create_user(email, password)
   
    for _ in range(10):
        score = randint(1,5)
        choice_movie = choice(movies_in_db)
        crud.create_rating(user, choice_movie, score)
    