"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def create_homepage():
    return render_template('homepage.html')

@app.route('/movies')
def show_movies():
    movies = crud.list_all_movies()
    return render_template("all_movies.html",movies=movies)

@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_users():
    users = crud.list_all_users()
    return render_template('all_users.html', users=users)



























if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
