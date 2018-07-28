# h5.3_Courses.py

import sys
from courses import Course, readCourses

# Read the course list
courseList = readCourses(sys.argv[1])

# Try to add one more course
courseList.append(Course("TIETA19", "Practical Programming in Python", 5, 5))

# Print out all types present in the courseList (should be only Course)
print(set(map(type, courseList)), end="\n\n")

# Print out all occurrences of course descriptions in the input (+ 1 added)
print("All course occurrences:")
for course in courseList:
  print(course)

# Print out only unique occurrences (based on course name)
print("\nUnique course occurrences:")
for course in sorted(set(courseList), key=str):
  print(course)