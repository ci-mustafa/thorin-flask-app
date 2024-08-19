from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask"


if __name__ == "__main__":
    app.run(
        # host = os.environ.get("IP", "0.0.0.0"),
        # port = int(os.environ.get("PORT", "5000")),
        debug = True   
    )
