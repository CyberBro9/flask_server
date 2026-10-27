from flask import *
from markupsafe import escape

database = []

class DataSet:
    name = ""
    password = ""
    email = ""

    def __init__(self, name, password, email=None):
        self.name = name
        self.password = password
        self.email = email if email else ""

app = Flask(__name__)

@app.route("/")
def does_any_function_name_work():
    return render_template("index.html")


@app.route("/login")
def sneaky():
    return render_template("login.html")


@app.route("/home")
def open_home():
    return render_template("home.html")

