from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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

# TODO: Fix Scope Issues - These should likely be inside the function or constants.
# TODO: PARAMS references 'query' which is undefined at this scope.
URL = "https://api.themoviedb.org/3/search/movie/"

# TODO: Security - Move API Key to environment variable or config file.
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGUzYjc5ZGRlMzMxMmUzZTgwYzUwNjE2YWUwZGMzYiIsIm5iZiI6MTc0ODk1NjEzMS43OTUsInN1YiI6IjY4M2VmM2UzNmE2MmY5MzBhNTI4OTgwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lXlg-yDfyD_hwaI0zDDYKBdBOy-yY2XmYM_OR5Psi5s"
}

# PARAMS ={
#    'query': query
# }

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_library.db"
db.init_app(app)

# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))


class EditForm(FlaskForm):
    # TODO: Data Type Mismatch - 'rating' should ideally be FloatField to ensure numeric input.
    rating = StringField("Your Rating Out of 10(e.g.: 7.5)", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

with app.app_context():
    db.create_all()

movies_data = []

def tmdb_fetch(query):
    # TODO: Fix Scope - pass 'query' to PARAMS here correctly.
    PARAMS = {'query': query}
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    data = response.json()
    data = data['results']
    return data

@app.route("/add_movie/<int:id>")
def add_movie(id):
    # TODO: Critical Logic Error - Fix URL formatting.
    # TODO: API Response Handling - 'results' key does not exist in single movie detail response.
    # TODO: Undefined Variable - 'data' is not defined in this scope.
    # TODO: Confused Logic - 'movie['results'][id]' is invalid structure.
    movie = requests.get(f'"https://api.themoviedb.org/3/movie/"{id}').json()
    movie = movie['results']
    movie = data['release_date']
    movie = movie['results'][id]
    new_movie = {}
    new_movie['year'] = movie['release_date'][:4]
    new_movie['img_url'] = f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}'
    new_movie.pop('poster_path')
    new_movie['description']= new_movie.pop('overview')
    new_movie['rating'] = new_movie.pop('vote_average')
    new_movie = Movie(**new_movie)
    db.session.add(new_movie)
    db.session.commit()
    return url_for("home")


@app.route("/")
def home():
    # TODO: Missing Ranking Logic - Update 'ranking' field based on sort order here.
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
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
    movie = db.session.get(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        data = tmdb_fetch(form.title.data)
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)