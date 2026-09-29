from student import Student
from classroom import Classroom
from allocator import allocate_students
from display import display_seating
from report import occupancy_report

students = []

n = int(input("Number of Students: "))

for i in range(n):

    reg = input("Register No: ")
    name = input("Name: ")
    sec = input("Section: ")

    students.append( Student(reg,name,sec) )

rows = int(input("Rows: "))
cols = int(input("Columns: "))

classroom = Classroom(rows, cols)

seating = allocate_students(
    students,
    rows,
    cols)

display_seating(seating)

occupancy_report(
    len(students),
    classroom.total_seats())
