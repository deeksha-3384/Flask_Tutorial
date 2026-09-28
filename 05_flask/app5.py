from flask import Flask, render_template

app5 = Flask(__name__)

@app5.route("/")
def home():
    return render_template("index.html")

@app5.route("/about")
def about():
    return render_template("about.html")

@app5.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app5.run(debug = True)