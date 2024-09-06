class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title

    def __repr__(self):
        return f"{self.course_id} - {self.title}"


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        if grade < 0:
            raise ValueError("Grade should be greater than zero")
        self.grade = grade

    def __repr__(self):
        return f"{self.course.title} - {self.student.name}: {self.grade if self.grade else "Not computed"}"


class College:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = set()

    def register_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = Student(student_id, name)

    def create_course(self, course_id, title):
        if course_id in self.courses:
            raise ValueError("Course ID already exists")
        self.courses[course_id] = Course(course_id, title)

    def enroll_student(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found")
        if course_id not in self.courses:
            raise ValueError("Course ID not found")
        student = self.students[student_id]
        course = self.courses[course_id]
        enrollment = Enrollment(student, course)
        self.enrollments.add(enrollment)

    def get_enrolled_courses(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found")
        return [enrollment.course for enrollment in self.enrollments if enrollment.student.student_id == student_id]

    def get_course_grades(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Course ID not found")
        return [enrollment for enrollment in self.enrollments if enrollment.course.course_id == course_id]
