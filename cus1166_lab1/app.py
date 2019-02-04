from mymodules.math_utils import average_grade
from mymodules.models import Student

def main():
    # create a roster of 10 students, print out
    # list of students, and print average score
    student_roster = [
        Student("Vinay Woodley", 67),
        Student("Abigail Monaghan", 76),
        Student("Menaal Johnston", 86),
        Student("Darrel Wooten", 91),
        Student("Danny Rooney", 69),
        Student("Ariel Whitfield", 73),
        Student("Emman Sanders", 88),
        Student("Milla Diaz", 97),
        Student("Eileen Landry", 56),
        Student("Joesph Guasp", 75)
        ]

    print("Student roster:")
    for student in student_roster:
        print(student.print_student_info())

    print(f"\nAverage: {average_grade(student_roster)}")

if __name__ == "__main__":
    main()