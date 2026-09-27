from flask import Flask
from uuid import UUID
app2 = Flask(__name__)
@app2.route("/")
def home():
    return "Welcome to  home page"

#URL CONVERTING : A converter lets you specify the type of that dynamic value
#integer, float, string converter
@app2.route("/details/<int:id>/<float:amount>/<string:name>")
def details(id,amount,name):
    return f"Name: {name} , ID: {id} , Amount: {amount}"

#Path converter : The path converter allows / inside the captured value
@app2.route("/files/<path:filename>")
def files(filename):
    return f"You requested: {filename}"

#uuid converter
@app2.route("/students/<uuid:user_id>")
def students(user_id):
    return str(user_id)

if __name__ == "__main__":
    app2.run(debug=True)