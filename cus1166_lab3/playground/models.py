from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "courses"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name=db.Column(db.String, nullable=False)
    course_title=db.Column(db.String, nullable=False)

    students = db.relationship("RegisteredStudent", backref="courses")

class RegisteredStudent(db.Model):
    __tablename__ = "registeredstudents"
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String, nullable=False)
    student_grade = db.Column(db.String, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"), nullable=False)


    