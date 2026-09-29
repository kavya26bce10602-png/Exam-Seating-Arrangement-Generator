def occupancy_report(
        total_students,
        total_seats):

    occupied = total_students

    percentage = ( occupied / total_seats ) * 100

    print("\n===== REPORT =====")

    print("Students :", occupied)
    print("Seats :", total_seats)
    print("Occupancy :", round(percentage,2), "%")