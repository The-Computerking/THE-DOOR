from Items import chestia
from Items import chestia2
from rn import doorhealthrandom
from rn import skinrandom
from rn import clawrandom
from rn import clawsharpnessrandom
from rn import creaturerandom
from rn import doorone
from descrypters import skin
from descrypters import teeth
from descrypters import clawsharpness
from descrypters import claws
from random import randint
import subprocess

playerhealth = 20
punch = 1
chest = "no"
healthdoor = doorhealthrandom
uc = creaturerandom
attack = "yes"
armourlvl = 0
print(" ")
print("Welcome to THE DOOR, a game created by Corin Dishon and Eli Wood")
print(f"{playerhealth} health")
print(" ")
invalid = True

while healthdoor > 0:
    print("there is a door")
    print(" ")
    # ptd = Punch The Door
    ptd = input("do you want to punch? ")

    if ptd == "yes" or ptd == "no" or ptd == "ptd":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        ptd = input("yes or no? ")
        if ptd == "yes" or ptd == "no" or ptd == "ptd":
            invalid = False
        else:
            continue

    if ptd == "no":
        print("You Turn Around and Leave")
        exit()
    elif ptd == "ptd":
        healthdoor = healthdoor - 10
    elif ptd == "yes":
        healthdoor = healthdoor - punch
        print(f"you did {punch} damage")
        print("door health ", healthdoor)
    else:
        continue
print(" ")
print("you destroyed it")
print(" ")
# laatd = Look Around After The Door
laatd = input("beyond the door you see a room, Do you want to look around? ")
print(" ")

invalid = True
if laatd == "yes" or laatd == "no":
    invalid = False

# more input validation
while invalid == True:
        print("wrong input")
        laatd = input("yes or no ")
        if laatd == "yes" or laatd == "no":
            invalid = False
        else:
            continue

if laatd == "yes":
    print("you enter the room inside is a chest")
    chest = input("do you want to open the chest ")
    print("")

    invalid = True
    if chest == "yes" or chest == "no":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        chest = input("yes or no?")
        if chest == "yes" or chest == "no":
            invalid = False
        else:
            continue

        if chest == "n":
            print("you headbutt the chest")
            exit()
        else:
            continue
print(f"you open the chest inside is {chestia}")
if chestia == "a sword" or chestia == "a mace" or chestia == "an axe" or chestia == "a spear":
    punch = punch + 4
    print(f"you do {punch} damage now")
elif chestia == "bread" or chestia == "an apple" or chestia == "a cookie":
    restorehealth = input("do you want to eat this and restore your health? ")

    invalid = True
    if restorehealth == "yes" or restorehealth == "no":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        restorehealth = input("yes or no?")
        if restorehealth == "yes" or restorehealth == "no":
            invalid = False
        else:
            continue

    if restorehealth == "yes":
        playerhealth = 20
        print("player health is now ", playerhealth)
    elif restorehealth == "no":
        leaveitem = input("do you want to leave this item? ")

        invalid = True
        if leaveitem == "yes" or leaveitem == "no":
            invalid = False

        # more input validation
        while invalid == True:
            print("wrong input")
            leaveitem = input("yes or no?")
            if leaveitem == "yes" or leaveitem == "no":
                invalid = False
            else:
                continue
        if leaveitem == "yes":
            print("you decide not to be a theif and leave the item")
        elif leaveitem == "no":
            print("you were so indecisive that you passed out")
        
elif chestia == "iron armour" or chestia == "leather armour" or chestia == "diamond armour":
    if chestia == "leather armour":
        armourlvl = armourlvl + 1
    elif chestia == "iron armour":
        armourlvl = armourlvl + 2
    elif chestia == "diamond armour":
        armourlvl = armourlvl + 3


print("You turn around and leave")
print(" ")