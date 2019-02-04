from mymodules.math_utils import average_grade
from mymodules.models import Student

def main():
    # create a roster of 10 students, print out
    # list of students, and print average score
    student_roster = [Student("Vinay Woodley", 67)]
    student_roster.append(Student("Abigail Monaghan", 76))
    student_roster.append(Student("Menaal Johnston", 86))
    student_roster.append(Student("Darrel Wooten", 91))
    student_roster.append(Student("Danny Rooney", 69))
    student_roster.append(Student("Ariel Whitfield", 73))
    student_roster.append(Student("Emman Sanders", 88))
    student_roster.append(Student("Milla Diaz", 97))
    student_roster.append(Student("Eileen Landry", 56))
    student_roster.append(Student("Joesph Guasp", 75))

    print("Student roster:")
    for student in student_roster:
        print(student.print_student_info())

    print(f"\nAverage: {average_grade(student_roster)}")

if __name__ == "__main__":
    main()