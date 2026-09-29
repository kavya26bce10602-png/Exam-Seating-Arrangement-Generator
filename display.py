def display_seating(seating):

    print("\nSEATING ARRANGEMENT\n")

    for row in seating:

        for seat in row:
            if seat:
                print(f"{seat.reg_no}", end="\t")
            else:
                print("EMPTY", end="\t")

        print()