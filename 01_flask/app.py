from flask import Flask 
#importing Flask class from flask library
#flask is already installed in venv (virtual envirnment)

app = Flask(__name__) #app is our actual web application
#Flask(__name__) creates the Flask application and tells Flask where this application lives.

@app.route("/")
def home():
    return "Welcome to home page"

# @app.route("/about")
# def about():
#     return "Welcome to about page "

# @app.route("/contact")
# def contact():
#     return "Welcome to contact page"
#Static route
@app.route("/users")
def users():
    return "Hello user"

#Dynamic route
@app.route("/user/<int:name>")
def user(name):
    return f"Hello {name}"

#Multiple dynamic parameters
@app.route("/student/<name>/<course>")
def student(name,course):
    return f"Hello {name} you are learning {course}"

if __name__ == "__main__":
    app.run(debug = True) 