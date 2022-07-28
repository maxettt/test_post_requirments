from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return "Введите слово"


@app.route("/search")
def search_page():
    s = request.args.get("s")
    if s:
        return f"Вы ввели слово {s}"
    return "Вы не ввели ничего"


@app.route("/filter")
def filter_page():
    f = request.args.get("from")
    t = request.args.get("to")
    if f and t:
        return f"Ищем в диапазоне от {f} до {t}"
    elif f and not t:
        return f"Ищем от {f}"
    elif not f and t:
        return f"Ищем до {t}"
    return "Ищем без фильтров"


app.run()