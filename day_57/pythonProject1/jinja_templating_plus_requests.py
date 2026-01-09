from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Go to /guess/<name> to see the real page</h1>'

@app.route('/guess/<name>')
def guess_page(name):
    AGIFY = f'https://api.agify.io?name={name}'
    GENDERIZE = f'https://api.genderize.io?name={name}'
    age = requests.get(AGIFY)
    gender = requests.get(GENDERIZE)
    return render_template('index.html', naming=name, age_num=age.json()['age'], manorwoman=gender.json()['gender'])

if __name__ == '__main__':
    app.run(debug=True)