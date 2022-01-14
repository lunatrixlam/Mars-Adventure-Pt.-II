# Mars Adventure, Part 2, link here: https://prep.hackbrightacademy.com/materials/prepr19/exercises/mars-2/

import random   # import random Module for door code later

import time     # for Mars landing and lift-off

geographic = ["mountains", "craters"]
life = ["ETs", "birds"]

geographic_count = 0
life_count = 0
boring_count = 0

while True:     # until no more observations, ask user for input and then note the observation

    observations = input("What do you see? ").lower()

    if observations == "":
        break
    if not observations.endswith("."):   # formats string to add a period at the end of input
        print(f"Noted: {observations}.")
    else:
        print(f"Noted: {observations}")
    
    # Categorize observation

    if ", " not in observations:
        observations = observations.split() # stores as list to iterate through and delimter at default in case input is separated by only spaces
    else:
        observations = observations.split(', ') # stores as list to iterate through and delimiter at ', ' in case input is separated by commas

    for observation in observations:

        found = False   # resets to False after running through each of the following for Loops

        for word in geographic: # for each element in geographic
            if observation in word.lower(): # if observations element in the geographic element
                geographic_count += 1
                found = True

        for word in life:   # for each element in life
            if observation in word.lower(): # if observations element in the life element
                life_count += 1
                found = True

        if found == False:  # if found never sets to True since the for Loop condition were not met
            boring_count += 1

print()
print("Finished observations.")
print(f"Geographic observations: {geographic_count}")
print(f"Life observations: {life_count}")
print(f"Boring observations: {boring_count}")
print()
print()

print("You are about to land on Mars!")
time.sleep(2)
print("...")
time.sleep(2)
print("The landing was successful.")
time.sleep(2)
print("Time to disembark!")
time.sleep(2)
print("...but first, you need to enter the door code to unlock the ship.")
print()

correct_code = str(random.randint(1000, 9999))  # grabs a random integer between 1000-9999 and returns it as a str so we can use the .isdigit() method later

num_guesses = 0     # initializes a counter variable to track guesses

print(f"Correct Code: {correct_code}")
print()

while True:

    guessed_code = input("Enter doorcode: ")

    if guessed_code.isdigit():
        if guessed_code == correct_code:
            break
        else:
            print("Sorry, that's wrong.")
            num_guesses += 1
            print(f"Wrong Guesses: {num_guesses}")
            print()
    else:
        print("Invalid door code. Enter 4 digits only.")
        print()

print()
print()
print("We're in. Welcome to Mars!")
print()
time.sleep(2)
print("...")
time.sleep(2)
print()
# A duel with Darth COBOL 

print("Oh, no! It's Darth COBOL! Time to duel.")
print()

darth_cobol_health = 3

while darth_cobol_health > 0:
    
    return_fire = input("Press RETURN to fire: ")

    if return_fire == "":
        if random.randint(1, 2) == 1:
            print("You missed!")
            print(f"Darth COBOL health: {darth_cobol_health}")
            print()
        else:
            print("You hit Darth COBOL!")
            darth_cobol_health -= 1
            print(f"Darth COBOL health: {darth_cobol_health}")
            print()
print("You win!")
print()

# Take-off from Mars and return home. Taking off from Mars is harder because of magic gamma rays so your spaceship needs to do the liftoff routine 3 times in a row.

print("This was a lot of fun. Now it's time to go home!")
print("Prepare for lift-off...")
print()

for i in range(3): # you can also use a While loop and initialize an attempt counter = 3 and nest the timer loop in the attempt While loop
    timer = 5

    while timer > 0:
        print(timer, "...")
        time.sleep(2)
        timer -= 1
print("*** LIFT-OFF ***")