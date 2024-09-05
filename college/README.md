# Advanced Student Enrollment System Exercise
An advanced student enrollment system manages courses, students, and instructors, along with course scheduling and prerequisites. The system should also handle grading, attendance tracking, and allow for course completion certificates.

**Features** 
The advanced student enrollment system should be able to perform the following operations:

1. **Register Student**: Register a new student with a unique student ID and name. Handle student information, such as courses completed, grades, and attendance records.
2. **Create Course**: Create a new course with a unique course ID, title, instructor, schedule, and optional prerequisites (i.e., courses that need to be completed before enrollment is allowed).
3. **Enroll Student**: Enroll a student in a course only if they have met the prerequisites. Students can only register for courses that do not conflict with their existing schedule.
4. **Track Attendance**: Record attendance for students in each course and generate attendance reports.
5. **Assign Grades**: Assign grades to students upon course completion and update their records.
6. **Issue Certificate**: Issue a course completion certificate to students who successfully complete a course with a passing grade.

**Conditions**  
- **Student**:
  - Each student must have a unique student ID and maintain records of their course completions, grades, and attendance.
  
- **Course**:
  - Each course must have a unique course ID, and optionally, prerequisites that students must complete before enrolling.
  - Courses must have a schedule (days and times), and students cannot enroll in overlapping courses.
  
- **Enrollment**:
  - Enrollment must validate both prerequisites and schedule conflicts.
  - Attendance and grades should be tracked for each student in each course.

- **Operations**:
  - Attendance records should be available for reporting, and grades should be recorded upon course completion.
  - Certificates should only be issued when a student meets the passing criteria.