from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/search')
def search_page():
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово {s}'
    return "Вы не ввели слово для поиска"


app.run()