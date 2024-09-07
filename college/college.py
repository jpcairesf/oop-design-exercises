class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        if grade < 0:
            raise ValueError("Grade should be greater than zero")
        self.grade = grade


class College:
    def __init__(self):
        self.students = {}
        self.courses = {}
        """
        This is a space efficient solution for enrollments.
        How would you implement a time efficient one?
        """
        self.enrollments = set()

    def register_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        if not name:
            raise ValueError("Invalid student name")
        self.students[student_id] = Student(student_id, name)

    def create_course(self, course_id, title):
        if course_id in self.courses:
            raise ValueError("Course ID already exists")
        if not title:
            raise ValueError("Invalid course title")
        self.courses[course_id] = Course(course_id, title)

    def enroll_student(self, student_id, course_id):
        self._validate_student(student_id)
        self._validate_course(course_id)
        student = self.students[student_id]
        course = self.courses[course_id]
        enrollment = Enrollment(student, course)
        self.enrollments.add(enrollment)

    def assign_grade(self, student_id, course_id, grade):
        self._validate_student(student_id)
        self._validate_course(course_id)
        for enrollment in self.enrollments:
            if enrollment.student.student_id == student_id and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                return
        raise ValueError("Student not enrolled in the given course")

    def get_course_grades(self, course_id):
        self._validate_course(course_id)
        enrollments = []
        for enrollment in self.enrollments:
            if enrollment.course.course_id == course_id:
                enrollments.append(enrollment)
        return enrollments

    def get_student_grades(self, student_id):
        self._validate_student(student_id)
        enrollments = []
        for enrollment in self.enrollments:
            if enrollment.student.student_id == student_id:
                enrollments.append(enrollment)
        return enrollments

    def _validate_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID not found")

    def _validate_course(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Course ID not found")
