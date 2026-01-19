from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page.
    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")

@app.route('/contact')
def contact():
    """
    Renders the contact page containing the login form.
    Returns:
        The rendered contacts.html template.
    """
    return render_template("contacts.html")

@app.route('/form-entry', methods=['GET', "POST"])
def forms():
      """
      Handles the form submission sent from the contact page.
      This route accepts POST requests containing the username and password.
      """
      return f"<h1>Username: {request.form['username']} Password: {request.form['password']} </h1>"


if __name__ == "__main__":
    app.run(debug=True)