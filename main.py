from training import Training
from database import Database


workout = Database()
workout.import_data()
first_try = Training(90, "ENG") #set duration and language ("PL"/"ENG")
pattern = (first_try.import_pattern())[0]
first_try.generate_plan(pattern)
first_try.print_training()

#saving (line below) is optional, it stores instructions in a txt file
#first_try.save_training()