# This is a quick workout randomizer to make it easy to decide what I want to do for my daily lunch workout.

import random

upperBodyExercises = ["Normal Pushups", "Hammer Curls", "Overhead Press", "Pike Pushups", "Shoulder Taps", "Forward QM",
                      "Weighted Curls", "Lateral Raises", "Diamond Pushups", "Handstand Hold"]

coreExercises = ["Hollow Body Hold", "V Ups", "Dragon Flags", "Superheros", "Crunches", "Mountain Climbers", "Leg Ups",
                 "Russian Twists", "Hold Boat"]

lowerBodyExercises = ["Air Squats", "Rail Balance", "Weighted Leg Raises", "Calf Raises", "One Leg Hops", "Backwards QM",
                "Single Leg Deadlifts", "Cossack Squats"]

cardioExercises = ["Sprint in Place", "Elliptical", "Ginga", "Run on Beach"]

userAnswer = " "
while userAnswer not in "cULC":
    userAnswer = input("""What type of exercise do you want? 'U' for Upper Body Exercises, 'C' for Core Exercises, 'L' for
Leg Exercises or 'c' for Cardio: """)

    if userAnswer == "c":
        userCardio = random.choice(cardioExercises)
        print(userCardio)

    elif userAnswer == "U" or userAnswer == "C" or userAnswer == "L":
        while True:
            try:
                numberOfExercises = int(input("How many exercises would you like to do? "))
            except ValueError:
                print("Sorry I didn't understand that.")
            else:
                break
        if userAnswer == "U":
            for i in range(0, int(numberOfExercises)):
                print(random.choice(upperBodyExercises))
        elif userAnswer == "C":
            for i in range(0, int(numberOfExercises)):
                print(random.choice(coreExercises))
        else:
            for i in range(0, int(numberOfExercises)):
                print(random.choice(lowerBodyExercises))
