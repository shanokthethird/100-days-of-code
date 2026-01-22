from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    LocationURL = StringField('Location URL', validators=[DataRequired(), URL()])
    OpeningTime = StringField('Opening Time', validators=[DataRequired()])
    ClosingTime = StringField('Closing Time', validators=[DataRequired()])
    CoffeeRating = SelectField(label='Coffee Rating', choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    WifiRating = SelectField(label='Wifi Rating', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    PowerRating = SelectField(label='Power Outlet Rating', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label='Submit')

# Exercise:
# TODO(done): add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# TODO(done): make coffee/wifi/power a select element with choice of 0 to 5.
# TODO(done): e.g. You could use emojis ☕️/💪/✘/🔌
# TODO(done): make all fields required except submit
# TODO(Done): use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = list(form.data.values())[:-2]
        with open("./day_62_flaskForm_project/cafe-data.csv", mode='a', encoding="utf-8") as csv_file:
            for data in new_cafe:
                if new_cafe.index(data) == 0:
                    csv_file.write(f"\n{data},")
                elif new_cafe.index(data) == 6:
                    csv_file.write(f"{data}")
                else:
                    csv_file.write(f"{data},")
        return render_template('add copy.html', form=form)
    # TODO(DONE):
        #Exercise:
        #Make the form write a new row into cafe-data.csv
        #with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./day_62_flaskForm_project/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
