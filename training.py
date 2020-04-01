from exercise import PL_Exercise
from exercise import ENG_Exercise
from datetime import date
from database import Database

class Training:
    def __init__(self, time, language="PL"):
        #self.type = type
        self.max_time = time
        self.current_time = 0
        self.number_of_exercises = 0
        self.exercises = []
        self.language = language

    def import_pattern(self):
        patterns = []
        default1 = {"WARMUP", "LEGS", "CHEST", "BACK", "ABS", "CARDIO"}
        patterns.append(default1)
        default2 = {"WARMUP", "BACK", "GLUTES", "ARMS", "CORE", "HIIT"}
        patterns.append(default2)
        self.number_of_exercises = 6
        return patterns


    def check_time(self):
        if ((self.max_time - self.current_time/60) > 15):
            return True
        else:
            return False


    def check_unique(self, exercise):
        for i in range (self.number_of_exercises):
            if (exercise.name == self.exercises[i]):
                return False
            else:
                return True


    def select_language(self, number):
        if (self.language == "PL"):
            exercise = PL_Exercise(number)
            return exercise
        if (self.language == "ENG"):
            exercise = ENG_Exercise(number)
            return exercise
        else:
            print("Unknown language chosen!")
            raise ValueError


    def add_exercise(self, type, number):
        exercise = self.select_language(number)
        exercise.generate_exercise(type)
        return exercise


    def generate_plan(self, pattern):
        data = Database()
        data.import_data()
        counter = 0
        for elem in pattern:
            counter += 1
            done = 0
            if self.check_time():
                while (done == 0):
                    exercise = self.add_exercise(elem, counter)
                    if ( (len(self.exercises) == 0) or self.check_unique(exercise)):
                        self.exercises.append(exercise)
                        self.current_time += exercise.totaltime
                        done = 1


    def save_training(self): #to txt file
        date = self.get_date()
        file = open(f"{date}.txt", "w")
        for elem in self.exercises:
            if (int(elem.weight) > 0):
                display = (str(int(elem.weight)) + "kg")
            elif (elem.weight == 0):
                display = (str(int(elem.workouttime)) + "s")
            else:
                raise ValueError
            file.write(f"{elem.name} \n {str(int(elem.series))} x {str(int(elem.reps))} || {display} \n\n")
        file.close()


    def get_date(self):
        today = date.today()
        return today


    def print_training(self):
        for elem in self.exercises:
            instructions = elem.print_exercise()
            print(instructions)
