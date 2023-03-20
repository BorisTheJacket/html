from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/working.html")
def web_site():
    return render_template('working.html')


@app.route("/future.html")
def future():
    return render_template('future.html')


if __name__ == "__main__":
    app.run(debug=True)