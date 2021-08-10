from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home(message=None):
  message = "Huzzah. Your n00b flask app is working."
  return render_template("main.html",message=message)