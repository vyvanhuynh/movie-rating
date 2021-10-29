""" To create function for CRUD operations """

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """ function to add new user to users table
        inputs: user's email and password        """

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """function to create a new movie
        inputs: title, overview, release_date, poster_path"""

    movie = Movie(title=title, 
                overview=overview, 
                release_date=release_date, 
                poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, score): 
    #   unsure of inputs for this function; tried vy@gmail.com, Dumbo, 9 but didnt work
    """ function to create and return a new rating """

    rat = Rating(score = score,
                 movie = movie,
                 user  = user ) 

    db.session.add(rat)
    db.session.commit()

    return rat

def list_all_movies():
    return Movie.query.all()

def get_movie_by_id(movie_id):  
    return Movie.query.get(movie_id)

def list_all_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()
    
def validate_login(email,password):
    return User.query.filter(User.email == email, User.password == password).first()




    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    