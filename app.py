from flask import Flask, render_template
from datetime import datetime
import re

app = Flask(__name__)

# replace the existing home with home template
@app.route("/")
def home():
    return render_template("home.html")

# new functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content
    # content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

    return render_template("hello_there.html", title=name, date=datetime.now())
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only
    match_object = re.match("[a-zA-z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name= "Friend"

    content = "Hello there, " + clean_name + "! It's" + formatted_now
    return content

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == '__main__': 
    app.run(host='127.0.0.1', debug=True, port=5000)