import requests
from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def home():
    BLOG = 'https://api.npoint.io/c790b4d5cab58020d391'
    all_posts = requests.get(BLOG).json()
    return render_template("index.html", blog_posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
