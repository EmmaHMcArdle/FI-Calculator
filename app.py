from flask import Flask, render_template
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/calculator")
def calculator():
    return render_template("one_time.html")

@app.route("/reoccuring_calculator")
def reoccuring_calculator():
    return render_template("reoccuring_calc.html")

if __name__ == '__main__':
    app.run(debug=True)