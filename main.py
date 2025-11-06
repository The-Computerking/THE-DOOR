from Items import chestia
from Items import chestia2
from Items import chestia3
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
from functions import inputvalidationdoor
from functions import inputvalidationchest
from functions import inputvalidationlookaround
from functions import chestfunction


playerhealth = 20
punch = 1
chest = "no"
healthdoor = doorhealthrandom
uc = creaturerandom
attack = "yes"
armourlvl = 0
armourslot = " "
weaponsslot = " "
itemsslots = []


def inventory():
    print("armour ", armourslot)
    print("weapon ", weaponsslot)
    print("items ", itemsslots)



print(" ")
print("Welcome to THE DOOR, a game created by Corin Dishon and Eli Wood")
print(f"{playerhealth} health")
print(" ")


while healthdoor > 0:
    print("there is a door")
    print(" ")
    # ptd = Punch The Door
    ptd = input("do you want to punch? ")

    inputvalidationdoor()

    if ptd == "no":
        print("You Turn Around and Leave")
        exit()
    elif ptd == "ptd":
        healthdoor = healthdoor - 10
    elif ptd == "yes":
        healthdoor = healthdoor - punch
        print(f"you did {punch} damage")
        print("door health ", healthdoor)

print(" ")
print("you destroyed it")
print(" ")
# laatd = Look Around After The Door
laatd = input("beyond the door you see a room, Do you want to look around? ")
print(" ")

inputvalidationlookaround

if laatd == "yes":
    print("you enter the room inside is a chest")
    chest = input("do you want to open the chest ")
    print("")

    inputvalidationchest()

    chestfunction()

elif laatd == "no":
    print("you turn around and leave ")
    exit

print("You turn around and leave")
print(" ")

healthdoor = doorhealthrandom

print("The next day you come back to the door")
print("And its back like it was never destroyed in the first place")
print(" ")

while healthdoor > 0:
    print("there is a door")
    # ptd = Punch The Door
    ptd = input("do you want to punch? ")
    print(" ")

    inputvalidationdoor()

    if ptd == "no":
        print("You Turn Around and Leave")
        print(" ")
        exit()
    if ptd == "ptd":
        healthdoor = healthdoor - 10
    elif ptd == "yes":
        print(healthdoor)
        healthdoor = healthdoor - punch
        print(f"you did {punch} damage")
        print(" ")

print("you destroyed it")
print("beyond the door you see a room, in the room you see an unknown creature")
print(" ")
laatd = input("do you want to enter? ")
print(" ")

inputvalidationlookaround()

skin = skin
skinrandom = skinrandom
teeth = teeth
claws = claws
clawsharpness = clawsharpness
creaturerandom = creaturerandom
clawrandom = clawrandom
clawsharpnessrandom = clawsharpnessrandom

if laatd == "yes":
    print("you enter the room")
    ptd = input("do you want to investigate? ")

    inputvalidationchest()

    if ptd == "yes":
        print(" ")
        print(f"you approach the creature and look closer its got {skin[skinrandom]} skin")
        print(f"and {teeth[skinrandom]} teeth and {claws[clawrandom]} {clawsharpness[clawsharpnessrandom]} claws")
        print("it gets up")
        print(" ")
        while attack == "yes" and uc >= 0:
            attack = input("do you want to punch ")

            invalid = True
            if attack == "yes" or attack == "no" or attack == "ptd":
                invalid = False
            elif attack == "inventory":
                inventory()
                invalid = False
            # more input validation
            while invalid == True:
                print("wrong input")
                attack = input("yes or no? ")
                if attack == "yes" or attack == "no" or attack == "ptd":
                    invalid = False

            if attack == "yes":
                print(f"you did {punch} damage")
                print("creature health", uc)
                print(" ")
                uc = uc - punch
                chance = randint(0, 10)
                if chance == 1:
                    playerhealth = playerhealth - 1
                    print("you take 1 damage")
                    print(playerhealth)
            elif attack == "no":
                print("you run")
                print("it chases you")
                if armourlvl > 0:
                    print("you turn around")
                    if teeth == "no" and claws == "no":
                        print("you escape")
                        exit()
                    elif teeth == "no":
                        print("it claws your armour protects you")
                        print("you escape")
                        continue
                    elif claws == "no":
                        print("it bites you your armour protects you")
                        print("you escape")
                        continue
                    elif claws != "no" and teeth != "no":
                        print("you get mauled to death")
                        print("your armour wasn't enough")
                        exit()
                elif chestia == "a sword" or "a mace" or "an axe" or "a spear":
                    attack = input("you sure you dont want to attack ")

                    invalid = True
                    if attack == "yes" or attack == "no" or attack == "ptd":
                            invalid = False
                    elif attack == "inventory":
                        inventory()
                        invalid = False

                    # more input validation
                    while invalid == True:
                        print("wrong input")
                        attack = input("yes or no? ")
                        if attack == "yes" or attack == "no" or attack == "ptd":
                            invalid = False
                        else:
                            continue

                else:
                    if teeth == "no" and claws == "no":
                        print("you escape ")
                        exit()
                    elif teeth == "no ":
                        print("it claws you you lose 2 health ")
                        playerhealth = playerhealth - 2
                        continue
                    elif claws == "no":
                        print("it bites you you lose 2 health")
                        print("you get thrown")
                        playerhealth = playerhealth - 2
                        continue
                    elif claws != "no" and teeth != "no":
                        print("you get mauled to death")
                        exit()
            elif attack == "ptd":
                uc = uc - 20

    elif ptd == "no":
        print("you did not approach the creature")
        print("you leave")
        print(" ")
        exit()
    

elif laatd == "no":
    print("you turn around and leave")

print(" ")
print("you killed it")
print("you go back to the door")
print("the floors gone")
print(" ")
chest = "n"
enterfloor = input("do you want to look into the floor? ")

invalid = True
if enterfloor == "yes" or enterfloor == "no":
    invalid = False
elif enterfloor == "inventory":
    inventory()
    invalid = False
# more input validation
while invalid == True:
    print("wrong input")
    enterfloor = input("yes or no? ")
    if enterfloor == "yes" or enterfloor == "no":
        invalid = False
    else:
        continue

if enterfloor == "yes":
    print(" ")
    print("you look into the floor")
    print("you see a room below")
    nextroom = input("do you want to enter next floor? ")
    print(" ")

    invalid = True
    if nextroom == "yes" or nextroom == "no":
        invalid = False
    elif nextroom == "inventory":
        inventory()
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        nextroom = input("yes or no? ")
        if nextroom == "yes" or nextroom == "no":
            invalid = False
        else:
            continue

    if nextroom == "yes":
        print("you drop down")
        laatd = input("Do you want to look around? ")
        print(" ")

        invalid = True
        if laatd == "yes" or laatd == "no":
            invalid = False
        elif laatd == "inventory":
            inventory()
            invalid = False

        # more input validation
        while invalid == True:
            print("wrong input")
            laatd = input("yes or no? ")
            if laatd == "yes" or laatd == "no":
                invalid = False
            else:
                continue

        if laatd == "yes":
            print("you enter the room inside there is a chest")
            while chest == "n":
                chest = input("do you want to open the chest ")
                print(" ")

                invalid = True
                if chest == "yes" or chest == "no":
                    invalid = False

                # more input validation
                while invalid == True:
                    print("wrong input")
                    chest = input("yes or no? ")
                    if chest == "yes" or chest == "no":
                        invalid = False
                    else:
                        continue

                if chest == "no":
                    print("ok")
                else:
                    continue
        elif laatd == "no":
            print("you pass out")
            exit


        print(f"you open the chest inside is a {chestia2}")
        if chestia2 == "a sword" or chestia2 == "a mace" or chestia2 == "an axe" or chestia2 == "a spear":
            punch = punch + 5
            weponsslot = chestia2
            print(f"you do {punch} damage now")
        elif chestia2 == "bread" or chestia2 == "an apple" or chestia2 == "a cookie":
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
                    storeitem = input("do you want to put this item in your inventory? ")

                    invalid = True
                    if storeitem == "yes" or storeitem == "no":
                        invalid = False

                    # more input validation
                    while invalid == True:
                        print("wrong input")
                        storeitem = input("yes or no?")
                        if storeitem == "yes" or storeitem == "no":
                            invalid = False
                        else:
                            continue
                    if storeitem == "yes":
                        itemsslots.append(chestia)
                        print("the item is now in your inventory ")
                    elif storeitem == "no":
                        print("you leave the item where you found it ")

        elif chestia2 == "iron armour" or chestia2 == "leather armour" or chestia2 == "diamond armour":
            if chestia2 == "leather armour":
                armourlvl = armourlvl + 1
                armourslot = chestia2
            elif chestia2 == "iron armour":
                armourlvl = armourlvl + 2
                armourslot = chestia2
            elif chestia2 == "diamond armour":
                armourlvl = armourlvl + 3
                armourslot = chestia2


        door = input("there are two doors which one do you want to enter ")
        print(" ")

        invalid = True
        if door == "1" or door == "2":
            invalid = False
        elif door == "inventory":
            inventory()
            invalid = False

        # more input validation
        while invalid == True:
            print("wrong input")
            door = input("1 or 2 ")
            if door == "1" or door == "2":
                invalid = False
            else:
                continue

        if door == "1":
            print("you enter door one")
            if doorone == 0:
                print("inside is the same creature you fought earlier")
                attack2 = "yes"
                uc = 20
                while attack2 == "yes" and uc != 0:
                    attack2 = input("do you want to attack ")

                    invalid = True
                    if attack2 == "yes" or attack2 == "no" or attack2 == "ptd":
                        invalid = False
                    elif attack2 == "inventory":
                        inventory()
                        invalid = False

                    # more input validation
                    while invalid == True:
                        print("wrong input")
                        attack2 = input("yes or no ")
                        if attack2 == "yes" or attack2 == "no" or attack2 == "ptd":
                            invalid = False
                        else:
                            continue

                    if attack2 == "yes":
                        print(f"you did {punch} damage")
                        print("creature health", uc)
                        print(" ")
                        uc = uc - punch
                        chance = randint(0, 10)
                        if chance == 1:
                            playerhealth = playerhealth - 1
                            print("you take 1 damage")
                            print(playerhealth)

                    elif attack2 == "no":
                        print("you run")
                        print("it chases you")
                        if armourlvl > 0:
                            print("you turn around")
                            if teeth == "no" and claws == "no":
                                print("you escape")
                                exit()
                            elif teeth == "no":
                                print("it claws your armour protects you")
                                print("you escape")
                                continue
                            elif claws == "no":
                                print("it bites you your armour protects you")
                                print("you escape")
                                continue
                            elif claws != "no" and teeth != "no":
                                print("you get mauled to death")
                                print("your weapon wasn't enough")
                                exit()
                        elif chestia == "sword" or "mace" or "axe" or "spear":
                            attack2 = input("you sure you dont want to attack ")

                            invalid = True
                            if attack2 == "yes" or attack2 == "yes" or attack2 == "ptd":
                                invalid = False
                            elif attack2 == "inventory":
                                inventory()
                                invalid = False

                            # more input validation
                            while invalid == True:
                                print("wrong input")
                                attack2 = input("yes or no ")
                                if attack2 == "yes" or attack2 == "no" or attack2 == "ptd":
                                    invalid = False
                                else:
                                    continue

                        else:
                            if teeth == "no" and claws == "no":
                                print("you escape ")
                                exit()
                            elif teeth == "no ":
                                print("it claws you you lose 2 health ")
                                playerhealth = playerhealth - 2
                                continue
                            elif claws == "no":
                                print("it bites you you lose 2 health")
                                print("you get thrown")
                                playerhealth = playerhealth - 2
                                continue
                            elif claws != "no" and teeth != "no":
                                print("you get mauled to death")
                                exit()
                            print("you killed it")
                            print("the floor collapses out from under you")
                    elif attack2 == "ptd":
                        uc = uc - 40
                        print("you killed it")
            elif doorone == 1:
                chest = "no"
                print("you enter the room inside there is a chest")
                while chest == "no":
                    chest = input("do you want to open the chest ")

                    invalid = True
                    if chest == "yes" or chest == "no":
                        invalid = False

                    # more input validation
                    while invalid == True:
                        print("wrong input")
                        chest = input("yes or no ")
                        if chest == "yes" or chest == "no":
                            invalid = False
                        else:
                            continue

                    if chest == "n":
                        print("ok")
                    else:
                        continue
                print(f"you open the chest inside is a {chestia3}")
                if chestia3 == "a sword" or chestia3 == "a mace" or chestia3 == "an axe" or chestia3 == "a spear":
                    punch = punch + 5
                    weponsslot = chestia3
                    print(f"you do {punch} damage now")

                elif chestia3 == "bread" or chestia3 == "an apple" or chestia3 == "a cookie":
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
                        storeitem = input("do you want to put this item in your inventory? ")

                        invalid = True
                        if storeitem == "yes" or storeitem == "no":
                            invalid = False

                        # more input validation
                        while invalid == True:
                            print("wrong input")
                            storeitem = input("yes or no?")
                            if storeitem == "yes" or storeitem == "no":
                                invalid = False
                            else:
                                continue
                        if storeitem == "yes":
                            itemsslots.append(chestia)
                            print("the item is now in your inventory ")
                        elif storeitem == "no":
                            print("you leave the item where you found it ")
                elif chestia3 == "iron armour" or chestia3 == "leather armour" or chestia3 == "diamond armour":
                    if chestia3 == "leather armour":
                        armourlvl = armourlvl + 1
                        armourslot = chestia3
                    elif chestia3 == "iron armour":
                        armourlvl = armourlvl + 2
                        armourslot = chestia3
                    elif chestia3 == "diamond armour":
                        armourlvl = armourlvl + 3
                        armourslot = chestia3

                print("the floor collapses from under you")
        elif door == "2":
            floordown = input("inside there is no floor do you want to go down another floor? ")

            invalid = True
            if floordown == "yes" or floordown == "no":
                invalid = False
            elif floordown == "inventory":
                inventory()
                invalid = False

            # more input validation
            while invalid == True:
                print("wrong input")
                floordown = input("yes or no ")
                if floordown == "yes" or floordown == "no":
                    invalid = False
                else:
                    continue

            if floordown == "yes":
                print("you go down a floor")
            elif floordown == "no":
                print("the floor collapses you go down a floor")



    elif nextroom == "no":
        print("you leave")
        exit
elif enterfloor == "no":
    print("you leave")
    exit

lookaround = input("do you want to look around ")
print(" ")

invalid = True
if lookaround == "yes" or lookaround == "no":
    invalid = False
elif lookaround == "inventory":
    inventory()
    invalid = False

# more input validation
while invalid == True:
    print("wrong input")
    lookaround = input("yes or no ")
    print(" ")
    if lookaround == "yes" or lookaround == "no":
        invalid = False
    else:
        continue


if lookaround == "yes":
    print("you look around")
    print("you see a door and a ladder ")
    print(" ")
elif lookaround == "no":
    print("you run head first into a wall ")
    exit()

doororladder = input("what do you want to do? ")
print(" ")

invalid = True
if doororladder == "door" or doororladder == "ladder":
    invalid = False
elif doororladder == "inventory":
    inventory()
    invalid = False

# more input validation
while invalid == True:
    print("wrong input")
    doororladder = input("door or ladder ")
    if doororladder == "door" or doororladder == "ladder":
        invalid = False
    else:
        continue


if doororladder == "door":
    print("you enter the door ")
    dungonmode = input("do you want to activate dungeon mode? ")

    invalid = True
    if dungonmode == "yes" or dungonmode == "no":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        dungonmode = input("yes or no ")
        if dungonmode == "yes" or dungonmode == "no":
            invalid = False
        else:
         continue


    if dungonmode == "yes":
        print("you activate dungeon mode")
        subprocess.run("python dungeonmode.py", shell=True)
    else:
        print("you leave")
elif doororladder == "use ladder":
    print("you use ladder to leave")
    end = input("do you want to end the game")

    invalid = True
    if floordown == "yes" or floordown == "yes":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        floordown = input("yes or no ")
        if floordown == "yes" or floordown == "no":
            invalid = False
        else:
            continue


    if end == "yes":
        exit()
    else:
        print("you go back down")
