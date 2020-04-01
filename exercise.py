from database import Database
from random import randint

class Exercise:
    def change_value(self, what, new_val):
        if (what == "series"):
            self.series = new_val
        if (what == "reps"):
            self.reps = new_val
        if (what == "weight"):
            self.weight = new_val
        if (what == "time"):
            self.workouttime = new_val
            self.totaltime = (self.series * (self.workouttime + self.breaktime) + 120)

    def __init__(self, number):
        self.name = ""
        self.series = 0
        self.reps = 0
        self.weight = 0
        self.workouttime = 0
        self.breaktime = 0
        self.totaltime = 0
        self.number = number


class PL_Exercise(Exercise):
    def __init__(self, number):
        super().__init__(number)

    def print_exercise(self):
        instruction = ""
        instruction += f"Cwiczenie nr: {self.number} \n"
        instruction += f"{self.name} \n"
        instruction += f"{self.series} x {self.reps}  || "
        if (self.weight != 0):
            instruction += (str(self.weight) + "kg")
        elif (self.weight == 0):
            instruction += (str(self.workouttime) + "s")
        instruction += "\n\n"
        return instruction

    def generate_exercise(self, type):
        table = Database()
        table.import_data()
        value = randint(0, len(table.DATA[type]) - 1)
        exercise = table.DATA[type][value]
        self.name = exercise[0]
        self.series = exercise[2]
        self.reps = exercise[3]
        self.weight = exercise[4]
        self.workouttime = exercise[5]
        self.breaktime = exercise[8]
        self.totaltime = (self.series * (self.workouttime + self.breaktime) + 120)


class ENG_Exercise(Exercise):
    def __init__(self, number):
        super().__init__(number)

    def print_exercise(self):
        instruction = ""
        instruction += f"Exercise no: {self.number} \n"
        instruction += f"{self.name} \n"
        instruction += f"{self.series} x {self.reps}  || "
        if (self.weight != 0):
            instruction += (str(self.weight) + "kg")
        elif (self.weight == 0):
            instruction += (str(self.workouttime) + "s")
        instruction += "\n\n"
        return instruction

    def generate_exercise(self, type):
        table = Database()
        table.import_data()
        value = randint(0, len(table.DATA[type]) - 1)
        exercise = table.DATA[type][value]
        self.name = exercise[1]
        self.series = exercise[2]
        self.reps = exercise[3]
        self.weight = exercise[4]
        self.workouttime = exercise[5]
        self.breaktime = exercise[8]
        self.totaltime = (self.series * (self.workouttime + self.breaktime) + 120)