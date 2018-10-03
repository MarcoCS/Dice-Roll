# Program name: main
import rollDie
import bizzBang
import Slots

        
def whatPlay(playerInp):  #Takes in player input as an Arg./Parameter to decide which program to run
    if playerInp == "roll die":
        print("You rolled:", rollDie.rollDie(int(input("What kind of dice?:"))))
    if playerInp == "bizzbang":
        print(bizzBang.bizzBang(int(input("What limit?"))))
    if playerInp == "slots":
        print(Slots.slots(int(input("How many rolls?"))))
while True:
    whatPlay(input("What do you want to play? (roll die, bizzbang, or slots:"))
