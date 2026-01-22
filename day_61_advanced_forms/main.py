from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
# Red underlines? Install the required packages first: 
# Open the Terminal in PyCharm (bottom left). 

# On Windows type:
# python -m pip install -r requirements.txt

# On MacOS type:
# pip3 install -r requirements.txt

# This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
bootstrap=Bootstrap5(app)

class MyForm(Form):
    email = StringField(label='E-mail: ', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password: ', validators=[InputRequired(), Length(min=8)])
    submit = SubmitField(label="Submit")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form=MyForm()
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
