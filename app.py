from flask import Flask 
#importing Flask class from flask library
#flask is already installed in venv (virtual envirnment)

app = Flask(__name__) #app is our actual web application
#Flask(__name__) creates the Flask application and tells Flask where this application lives.
#When you're running this file directly, Python sets: __name__ = "__main__"

@app.route("/")
def home():
    return "Hello Flask"

if __name__ == "__main__":
    app.run(debug = True) 