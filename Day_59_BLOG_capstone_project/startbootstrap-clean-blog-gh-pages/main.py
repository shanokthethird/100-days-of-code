from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    return render_template("post.html", post_id=index)


if __name__ == "__main__":
    app.run(debug=True)
