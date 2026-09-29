class Student:
    def __init__(self, reg_no, name, section):
        self.reg_no = reg_no
        self.name = name
        self.section = section

    def __str__(self):
        return f"{self.reg_no} - {self.section}"