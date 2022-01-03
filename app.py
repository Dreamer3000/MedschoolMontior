from flask import Flask, render_template
from flask_navigation import Navigation, navbar, item
app = Flask(__name__)
nav = Navigation(app)




@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/hours")
def hours():

    return render_template("hours.html")

@app.route("/stats")
def stats():

    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True, port = 4000)
