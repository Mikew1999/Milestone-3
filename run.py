import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", page_title="blog")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("Port", "5000")),
        debug=True
    )
