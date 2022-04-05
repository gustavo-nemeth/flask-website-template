from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['TESTING'] = True
Bootstrap(app)


@app.route("/")
def view_home():
    return render_template("home.html", title="Inicio")


@app.route("/info")
def view_info():
    return render_template("info.html", title="Informações")


@app.route("/contato")
def view_contato():
    return render_template("contato.html", title="Contato")


if __name__ == '__main__':
    app.run(debug=True)
