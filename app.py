from flask import *
from werkzeug.security import check_password_hash, generate_password_hash
import db
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "IJUSTHITTHEJACKPOT67"
app.config.database = "database/flaskr.sqlite"

def create_app():
    db.init_app(app)


def login(username, password):
    data = db.get_db()
    error = None
    user = data.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']

    return error


def register(username, password):
    data = db.get_db()
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    if error is None:
        try:
            data.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            data.commit()
        except data.IntegrityError:
            error = f"User {username} is already registered."

    return error


@app.route("/")
def does_any_function_name_work():
    return render_template("index.html")


@app.route("/login", methods=("GET", "POST"))
def login_request():
    if request.method == "POST":
        error = login(request.form["name"], request.form["password"])
        if error:
            flash(error)
        else:
            return redirect("/home")

    return render_template("login.html")


@app.route("/login/newuser", methods=("GET", "POST"))
def register_request():
    if request.method == "POST":
        error = register(request.form["name"], request.form["password"])
        if error:
            flash(error)
        else:
            return redirect("/home")

    return render_template("login.html")


@app.route("/home")
def open_home():
    if session["user_id"]:
        return render_template("home.html")

    return redirect("/login")


@app.context_processor
def set_user_data():
    data = db.get_db()
    user = data.execute(
        'SELECT * FROM user WHERE id = ?', (session["user_id"],)
    ).fetchone()

    return dict(username = user["username"], id = user["id"])
