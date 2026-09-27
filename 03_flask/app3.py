from flask import Flask , request

app3 = Flask(__name__)

#Query Parameters : Query parameters are extra information you attach to the URL after ?
@app3.route("/search")
def search():
    name = request.args.get("name", "Guest") #Guest is the default value if there is no name
    #If there is no default value it returns "None"
    course = request.args.get("course", "Unknown")
    # return f"Hello {name}" #http://127.0.0.1:5000/search?name=Deeksha (Displays "Hello Deeksha")
    return f"{name} is learning {course}" #http://127.0.0.1:5000/search?name=Riya&course=Data%20Science (Displays "Riya is learning Data Science")

if __name__ == "__main__":
    app3.run(debug = True)