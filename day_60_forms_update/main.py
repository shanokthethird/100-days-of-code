from flask import Flask, render_template, request
import requests, smtplib
from email.mime.text import MIMEText

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)
URL_EMAIL = 'smtp.gmail.com'
MY_EMAIL = 'xxshanok3xx@gmail.com'
PASSWORD = 'zizb qfxw igpn fhsp'
char_index = 6
letter = ''


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)
        body = f"Email: {data['email']}\nPhone: {data['phone']}\n\nMessage: {data["message"]}"
        message = MIMEText(body, "plain")
        message["Subject"] = f'Blog Contact from {data["name"]}'
        message["From"] = MY_EMAIL 
        message["To"] = MY_EMAIL
        with smtplib.SMTP(URL_EMAIL) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, message.as_string())
        return "<h1>Email sent successfully!</h1>"
    elif request.method == "GET":
        return render_template("contact.html")
        

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
