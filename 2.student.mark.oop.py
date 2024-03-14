class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"{self.course_id} - {self.name}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)

    def input_student_marks(self):
        course_id = input("Enter course ID: ")
        for student in self.students:
            mark = float(input(f"Enter the mark for {student.name} in {course_id}: "))
            student.add_mark(course_id, mark)

    def list_students(self):
        if not self.students:
            print("There aren't any students yet")
        else:
            print("This is the student list: ")
            for i, student in enumerate(self.students, start=1):
                print(f"{i}. {student}")
                if student.marks:
                    print("Marks (Course ID - Mark):", student.marks)

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses yet")
        else:
            print("This is the course list: ")
            for i, course in enumerate(self.courses, start=1):
                print(f"{i}. {course}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to show student marks: ")
        print(f"Student marks for course {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name}: {student.marks[course_id]}")

    def main(self):
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
                self.input_students()
            elif option == 2:
                self.input_courses()
            elif option == 3:
                if not self.students or not self.courses:
                    print("Input students and courses first.")
                else:
                    self.input_student_marks()
            elif option == 4:
                self.list_students()
            elif option == 5:
                self.list_courses()
            elif option == 6:
                if not self.students or not self.courses:
                    print("Input students and courses first.")
                else:
                    self.show_student_marks()
            else:
                print("Invalid input. Please try again!")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.main()