## College Exercise

A college is responsible for managing student registrations, course creation, and enrollments. The system must also keep track of which students are enrolled in which courses and allow retrieval of this information.

### Features

The student enrollment system should be able to perform the following operations:

1. **Register Student**: Register a new student with a unique student ID and name.
2. **Create Course**: Create a new course with a unique course ID and title.
3. **Enroll Student**: Enroll a registered student in a course.
4. **Get Enrolled Courses**: Retrieve a list of courses that a specific student is enrolled in.
5. **Get Enrolled Students**: Retrieve a list of students enrolled in a specific course.

### Conditions

**Student**:
- Each student must have a unique student ID.
- The student ID should be greater than zero.

**Course**:
- Each course must have a unique course ID.
- The course ID should be greater than zero.

**Enrollment**:
- A student must be registered in the system before enrolling in a course.
- A course must be created in the system before students can enroll.
- Students can be enrolled in multiple courses, and a course can have multiple students.
- Operations should ensure that enrollments are properly tracked and that information can be retrieved correctly.