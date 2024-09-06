import unittest
import college


class TestCollege(unittest.TestCase):
    def setUp(self):
        self.college = college.College()

    def test_register_student(self):
        pass

    def test_register_student_already_exists(self):
        pass

    def test_create_course(self):
        pass

    def test_create_course_already_exists(self):
        pass

    def test_enroll_student(self):
        pass

    def test_enroll_student_not_found_student(self):
        pass

    def test_enroll_student_not_found_course(self):
        pass

    def test_get_enrolled_courses(self):
        pass

    def test_get_enrolled_courses_not_found(self):
        pass

    def test_get_course_grades(self):
        pass

    def test_get_course_grades_not_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
