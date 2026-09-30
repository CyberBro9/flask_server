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


@app.route("/slinkaway")
def sneaky():
    return render_template("slinkaway.html")


@app.route("/slinkaway/<int:repeats>")
def sneaky_count(repeats: int):
    string = ""
    for i in range(repeats):
        string += f"this text will now be displayed {escape(repeats)} times</br>"

    return f"<p>{string}</p>"