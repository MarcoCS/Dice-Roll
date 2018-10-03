# Program name: Slots
# Purpose: to play slots
# Creator: Marco
# --------------------------------

import random

possibleRoll = ["fish", "turtle", "potato", "salad", "watermelon"]
def slots(Rolls):  # Rolls is the argument for how many slots we are running
    storedRoll = []
    for x in range(Rolls):  # rolls x amount of slots 
        storedRoll.append(possibleRoll[random.randint(0,4)])
    for x in range(Rolls):
        if storedRoll.count(storedRoll[x]) == Rolls: #Go through the entire list iteratively
            return ("You win! Your roll was:{}" .format(storedRoll))
        else:
            return ("You lose! Your roll was:{}" .format(storedRoll))

