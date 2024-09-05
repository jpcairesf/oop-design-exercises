class Student:
    """Represents a student with a unique ID and name."""
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Course:
    """Represents a course with a unique ID and title."""
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title

class Enrollment:
    """Represents an enrollment of a student in a course."""
    def __init__(self, student, course):
        self.student = student
        self.course = course

class EnrollmentSystem:
    """Manages student enrollments and courses."""
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = []

    def register_student(self, student_id, name):
        """Register a new student with a unique ID and name."""
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = Student(student_id, name)

    def create_course(self, course_id, title):
        """Create a new course with a unique ID and title."""
        if course_id in self.courses:
            raise ValueError("Course ID already exists")
        self.courses[course_id] = Course(course_id, title)

    def enroll_student_in_course(self, student_id, course_id):
        """Enroll a registered student in a course."""
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        if course_id not in self.courses:
            raise ValueError("Course ID does not exist")
        student = self.students[student_id]
        course = self.courses[course_id]
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)

    def get_enrolled_courses(self, student_id):
        """Retrieve the list of courses a student is enrolled in."""
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        return [enrollment.course.title for enrollment in self.enrollments if enrollment.student.student_id == student_id]

    def get_enrolled_students(self, course_id):
        """Retrieve the list of students enrolled in a course."""
        if course_id not in self.courses:
            raise ValueError("Course ID does not exist")
        return [enrollment.student.name for enrollment in self.enrollments if enrollment.course.course_id == course_id]
