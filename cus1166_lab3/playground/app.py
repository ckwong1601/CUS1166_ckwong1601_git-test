import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route("/add_course", methods = ["POST"])
def add_course():
    name = request.form.get("name")
    title = request.form.get("title")

    course = Course(course_name=name, course_title=title)
    db.session.add(course)
    db.session.commit()

    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route("/register_student/<int:course_id>", methods = ["GET", "POST"])
def register_student(course_id):
    course = Course.query.get(course_id)
    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")
        student = RegisteredStudent(student_name=name, student_grade=grade, course_id=course_id)
        db.session.add(student)
        db.session.commit()
    
    students = course.students
    print(students)
    return render_template("course_details.html", course=course, students=students)

@app.route("/search_course", methods=["POST"])
def search_course():
    keyword = request.form.get("keyword")
    courses = Course.query.filter((Course.course_name.contains(keyword) | Course.course_title.contains(keyword)))
    return render_template("index.html", courses=courses)