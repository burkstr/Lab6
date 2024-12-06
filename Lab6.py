import pickle
class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []
    def get_details(self):
        self.course_name = input("Enter the course name: ")
        rangenum = int(input("How many Students and grades would you like to enter?: "))
        for x in range(rangenum):
            student_id = input("Student ID: ")
            grade = int(input("Grade (0-100): "))
            while grade < 0 or grade > 100:
                print("Grade must be between 0 and 100. Please enter again.")
                grade = int(input("Grade: "))
            self.stu_ID.append(student_id)
            self.stu_grade.append(grade)
    def display(self):
        print("Course Name:", self.course_name)
        for student_id, grade in zip(self.stu_ID, self.stu_grade):
            print("Student ID:", student_id)
            print("Grade:", grade)
        print()
courses = []
c_rangenum = int(input("How many courses would you like to add?: "))
for i in range(c_rangenum):
    print(f"Enter details for Course {i + 1}:")
    course = Course_grades()
    course.get_details()
    courses.append(course)
with open('grades_info.dat', 'ab') as f:
    for course in courses:
        pickle.dump(course, f)
print("\nReading and displaying objects from file:")
with open('grades_info.dat', 'rb') as f:
    while True:
        try:
            course = pickle.load(f)
            course.display()
        except EOFError:
            break

