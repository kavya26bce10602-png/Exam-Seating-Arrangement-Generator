class Classroom:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def total_seats(self):
        return self.rows * self.cols