from flask import Flask, render_template
import os
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    p_title = "About"
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = p_title, company = data)


@app.route("/contact")
def contact():
    p_title = "Contact"
    return render_template("contact.html", page_title = p_title)


@app.route("/careers")
def careers():
    p_title = "Careers"
    return render_template("careers.html", page_title = p_title)


if __name__ == "__main__":
    app.run(
        # host = os.environ.get("IP", "0.0.0.0"),
        # port = int(os.environ.get("PORT", "5000")),
        debug = True   
    )
