import unittest
import college


class TestCollege(unittest.TestCase):
    def setUp(self):
        self.college = college.College()

    def test_register_student(self):
        self.college.register_student(1, "Student 1")
        self.assertIn(1, self.college.students)
        self.assertEqual(1, len(self.college.students))

    def test_register_student_already_exists(self):
        self.college.register_student(1, "Student 1")
        with self.assertRaises(ValueError):
            self.college.register_student(1, "Student 2")

    def test_create_course(self):
        self.college.create_course(1, "Course 1")
        self.assertIn(1, self.college.courses)
        self.assertEqual(1, len(self.college.courses))

    def test_create_course_already_exists(self):
        self.college.create_course(1, "Course 1")
        with self.assertRaises(ValueError):
            self.college.create_course(1, "Course 2")

    def test_enroll_student(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.assertEqual(1, next(iter(self.college.enrollments)).student.student_id)
        self.assertEqual(1, next(iter(self.college.enrollments)).course.course_id)
        self.assertEqual(None, next(iter(self.college.enrollments)).grade)

    def test_enroll_student_not_found_student(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        with self.assertRaises(ValueError):
            self.college.enroll_student(2, 1)

    def test_enroll_student_not_found_course(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        with self.assertRaises(ValueError):
            self.college.enroll_student(1, 2)

    def test_assign_grade(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.college.assign_grade(1, 1, 10)
        self.assertEqual(10, next(iter(self.college.enrollments)).grade)

    def test_assign_grade_invalid_grade(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        with self.assertRaises(ValueError):
            self.college.assign_grade(1, 1, -1)

    def test_assign_grade_not_found_student(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        with self.assertRaises(ValueError):
            self.college.assign_grade(2, 1, 10)

    def test_assign_grade_not_found_course(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        with self.assertRaises(ValueError):
            self.college.assign_grade(1, 2, 10)

    def test_assign_grade_student_not_enrolled(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        with self.assertRaises(ValueError):
            self.college.assign_grade(1, 1, 10)

    def test_get_course_grades(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.college.assign_grade(1, 1, 10)
        course_grades = self.college.get_course_grades(1)
        self.assertEqual(1, len(course_grades))

    def test_get_course_grades_not_found_course(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.college.assign_grade(1, 1, 10)
        with self.assertRaises(ValueError):
            self.college.get_course_grades(2)

    def test_get_student_grades(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.college.assign_grade(1, 1, 10)
        student_grades = self.college.get_student_grades(1)
        self.assertEqual(1, len(student_grades))

    def test_get_student_grades_not_found_student(self):
        self.college.register_student(1, "Student 1")
        self.college.create_course(1, "Course 1")
        self.college.enroll_student(1, 1)
        self.college.assign_grade(1, 1, 10)
        with self.assertRaises(ValueError):
            self.college.get_student_grades(2)


if __name__ == '__main__':
    unittest.main()
