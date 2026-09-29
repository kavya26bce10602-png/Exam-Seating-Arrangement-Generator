def allocate_students(students, rows, cols):

    students.sort(key=lambda x: x.section)

    seating = []

    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            if index < len(students):
                row.append(students[index])
                index += 1
            else:
                row.append(None)

        seating.append(row)

    return seating