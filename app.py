from flask import *
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def does_any_function_name_work():
    return "<p>yo what's up?</p>"


@app.route("/slinkaway")
def sneaky(repeats: int):
    return "<p>you're quite the sneaky individual</p>"


@app.route("/slinkaway/<int:repeats>")
def sneaky_count(repeats: int):
    string = ""
    for i in range(repeats):
        string += f"this text will now be displayed {escape(repeats)} times "

    return f"<p>{string}</p>"