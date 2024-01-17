def input_students():
    students = []
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = {"id": student_id, "name": name, "dob": dob, "marks": {}}
        students.append(student)
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {"id": course_id, "name": name}
        courses.append(course)
    return courses

def input_student_marks(students):
    course_id = input(" Marks for student in this course: ")
    for student in students:
        mark = float(input(f"Enter the mark for {student['name']} in {course_id}: "))
        student['marks'][course_id] = mark

def list_courses(courses):
    if not courses:
        print("There aren't any courses yet")
    else:
        print("This is the course list: ")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course['id']} - {course['name']}")

def list_students(students):
    if not students:
        print("There aren't any students yet")
    else:
        print("This is the student list: ")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['id']} - {student['name']} - {student['dob']}")
            if student['marks']:
                print("Marks (Course Id - Mark):", student['marks'])

def show_student_marks(students):
    course_id = input("Enter the course ID to show student marks: ")
    print(f"Student marks for course {course_id}:")
    for student in students:
        if course_id in student['marks']:
            print(f"{student['name']}: {student['marks'][course_id]}")

def main():
    students = []
    courses = []

    while True:
        print("""
    0. Exit
    1. Input Students
    2. Input Courses
    3. Input Student Mark
    4. List Students
    5. List Courses
    6. Show Student Marks
    """)
        option = int(input("Your choice: "))

        if option == 0:
            break
        elif option == 1:
            students = input_students()
        elif option == 2:
            courses = input_courses()
        elif option == 3:
            if not students or not courses:
                print(" input students and courses first.")
            else:
                input_student_marks(students)
        elif option == 4:
            list_students(students)
        elif option == 5:
            list_courses(courses)
        elif option == 6:
            if not students or not courses:
                print(" input students and courses first.")
            else:
                show_student_marks(students)
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
