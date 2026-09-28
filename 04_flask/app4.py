from flask import Flask , render_template

app4 = Flask(__name__)

@app4.route("/")
def home():
    # return "<h1>Welcome to home page<h1>" # works but not recommended
    name = "Deeksha"
    course = "Data Science"
    city = "Bengaluru"
    return render_template("index.html" , name=name, course=course, city=city)

@app4.route("/detail")
def detail():
    first_name = "Roronoa"
    last_name = "Zoro"
    age = 22
    price = 2000
    courses = [
        "java","python","c programming","r programming"
    ]
    return render_template("market.html", first_name=first_name, last_name=last_name, age=age, price=price, courses=courses)

@app4.route("/ifelseexample")
def ifelseexample():
    is_true = True #or False
    old_user = False
    marks = 80
    return render_template("ifelse.html", is_true=is_true, old_user=old_user, marks=marks)

@app4.route("/forexample")
def forexample():
    courses = [ "Java", "Python", "Flask", "Springboot"]
    details = {
        "Name" : "Deeksha",
        "Age" : 20,
        "Course" : "Data Science"
    }
    return render_template("for.html", courses=courses, details=details)
if __name__ == "__main__":
    app4.run(debug = True)
