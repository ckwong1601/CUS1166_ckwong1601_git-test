from flask import Flask, render_template

app = Flask(__name__)
class_roster = [
    ("Johnny Zucchero", "B", "Senior"),
    ("Paige Fredrica", "A", "Sophmore"),
    ("Scott Haas", "C", "Senior"),
    ("Nick Bauer", "B", "Freshman"),
    ("Casey Krueger", "A", "Junior"),
    ("Lucas Detrick", "B", "Sophmore"),
    ("Derek Hatfield", "B", "Junior"),
    ("Megan Mcnamara", "C", "Freshman"),
    ("Joesph Hammond", "A", "Senior"),
    ("Lake Anthony", "B", "Freshman")
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name.capitalize())

@app.route("/roster/<grade_view>")
def roster(grade_view):
    print(grade_view)
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()