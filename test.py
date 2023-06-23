from flask import Flask, render_template, make_response, redirect, url_for, request, session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb02820a3e94d72c9f950ee10ef7e3f7a35b3f5b'
app.permanent_session_lifetime = datetime.timedelta(days=10)

menu = [{"title": "Главная", "url": "index"},
        {"title": "Добавить статью", "url": "add_post"}]


# @app.route("/")
# def index():
#     return render_template('index.html', menu=menu, posts=[])

# @app.route("/")
# def index():
#     content = render_template('index.html', menu=menu, posts=[])
#     res = make_response(content)
#     res.headers['Content-Type'] = 'text/plain'
#     res.headers['Server'] = 'flasksite'
#     return res

# @app.route("/")
# def index():
#     img = None
#     with app.open_resource(app.root_path + "/static/img/1.png", mode="rb") as f:
#         img = f.read()
#     if img is None:
#         return "None image"
#     res = make_response(img)
#     res.headers['Content-Type'] = 'image/png'
#     return res

# @app.route('/transfer')
# def transfer():
#     return redirect(url_for('index'), 301)

@app.route("/add_post")
def add_post():
    return 0

# @app.route("/")
# def index():
#     res = make_response("<h1>Hello</h1>", 200)
#     return res

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновление данных сессии
    else:
        session['visits'] = 1  # запись данных в сессию

    return f"<h1>Main Page</h1>Число просмотров: {session['visits']}"


@app.route("/login")
def login():
    log = ""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')
    res = make_response(f"<h1>Форма авторизации</h1>logged: {log}")
    res.set_cookie("logged", "yes")
    return res


data = [1, 2, 3, 4]
@app.route("/session")
def session_data():
    session.permanent = True
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True

    return f"session['data']: {session['data']}"
#
# @app.route("/logout")
# def logout():
#     res = make_response("Вы больше не авторизованы!</p>")
#     res.set_cookie("logged", "", 0)
#     return res


if __name__ == "__main__":
    app.run(debug=True)