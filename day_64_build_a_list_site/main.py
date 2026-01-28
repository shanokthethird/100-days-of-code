from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# PARAMS ={
#    'query': query
# }

app = Flask(__name__)
# Configure the secret key for Flask-WTF forms
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Initialize Bootstrap-Flask
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

# Initialize SQLAlchemy
db = SQLAlchemy(model_class=Base)
# Configure the SQLite database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_library.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    """
    Movie Database Model.
    Represents the 'movie' table in the database.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))


class EditForm(FlaskForm):
    """
    Form for editing movie details (rating and review).
    """
    rating = FloatField("Your Rating Out of 10(e.g.: 7.5)", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    """
    Form for adding a new movie by title.
    """
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# Create database tables within the application context
with app.app_context():
    db.create_all()

movies_data = []

def tmdb_fetch(query):
    """
    Fetches movie data from the TMDB API based on a search query.
    
    Args:
        query (str): The movie title to search for.
        
    Returns:
        list: A list of movie dictionaries returned by the API.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGUzYjc5ZGRlMzMxMmUzZTgwYzUwNjE2YWUwZGMzYiIsIm5iZiI6MTc0ODk1NjEzMS43OTUsInN1YiI6IjY4M2VmM2UzNmE2MmY5MzBhNTI4OTgwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lXlg-yDfyD_hwaI0zDDYKBdBOy-yY2XmYM_OR5Psi5s"
    }
    params = {'query': query}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    data = data['results']
    return data

@app.route("/add_movie/<int:id>")
def add_movie(id):
    """
    Route to add a specific movie selected from the search results.
    Fetches detailed movie data and saves it to the database.
    
    Args:
        id (int): The TMDB movie ID.
    """
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGUzYjc5ZGRlMzMxMmUzZTgwYzUwNjE2YWUwZGMzYiIsIm5iZiI6MTc0ODk1NjEzMS43OTUsInN1YiI6IjY4M2VmM2UzNmE2MmY5MzBhNTI4OTgwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lXlg-yDfyD_hwaI0zDDYKBdBOy-yY2XmYM_OR5Psi5s"
    }
    movie = requests.get(f'https://api.themoviedb.org/3/movie/{id}', headers=headers).json()
    new_movie = {'ranking': '', 'review': ''}
    new_movie['year'] = movie['release_date'][:4]
    new_movie['img_url'] = f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}'
    new_movie['description']= movie.pop('overview')
    new_movie['rating'] = movie.pop('vote_average')
    new_movie['title'] = movie.pop('title')
    new_movie = Movie(**new_movie)
    try:
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    except:
        return redirect(url_for("home"))


@app.route("/")
def home():
    """
    Home route. Displays all movies in the database, sorted by rating.
    """
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    movies.sort(key=lambda x: x.rating, reverse=True)
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """
    Edit route. Allows updating a movie's rating and review.
    
    Args:
        id (int): The ID of the movie to edit.
    """
    movie = db.session.get(Movie, id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    """
    Delete route. Removes a movie from the database.
    
    Args:
        id (int): The ID of the movie to delete.
    """
    movie = db.session.get(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Add route. Displays the search form and results for adding a new movie.
    """
    form = AddForm()
    if form.validate_on_submit():
        data = tmdb_fetch(form.title.data)
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
