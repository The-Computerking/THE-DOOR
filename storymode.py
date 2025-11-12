print("to be made")
exit

#import statments
from Items import chestia
from Items import chestia2
from Items import chestia3
from Items import items
from rn import smdhr
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

#inventory stuff
def inventory():
    print("armour ", armourslot)
    print("weapon ", weaponsslot)
    print("items ", itemsslots)

def doorfight():
    healthdoor = randint(1, 5)
    while healthdoor > 0:
            print("there is a door")
            print(" ")
            # ptd = Punch The Door
            ptd = input("do you want to punch? ")
            if ptd == "inventory":
                inventory()
            invalid = True
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


#varibles
playerhealth = 20
punch = 1
chest = "no"
healthdoor = smdhr
uc = creaturerandom
attack = "yes"
armourlvl = 0
armourslot = " "
weaponsslot = " "
itemsslots = []

#what certain varibles mean
#ptd = punch the door
#wdtwtd = what do you want to do


#story mode game
print("you awake in an abondoned city ")
print("you have no memory of who you are ")
print("what you are or what happened to the city")

door = input("you see a building do you want to enter it ")
if door == "inventory":
    inventory()
invalid = True
if door == "yes" or door == "no" :
    invalid = False


# more input validation
while invalid == True:
    print("wrong input")
    door = input("yes or no? ")
    if door == "yes" or door == "no":
        invalid = False
    else:
        continue

if door == "no":
    print("you turn round and bam you die")
elif door == "yes":
    print("you try the door its locked ")
    while healthdoor > 0:
        print("there is a door")
        print(" ")
        # ptd = Punch The Door
        ptd = input("do you want to punch? ")
        if ptd == "inventory":
            inventory()
        invalid = True
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

print(" ")
print("you destroyed it")
print(" ")
print("you go inside and see a room with a chest and a door ")
wdtwtd = input("what do you want to do chest or door? ")
if wdtwtd == "inventory":
    inventory()
invalid = True
if wdtwtd == "chest" or wdtwtd == "door":
    invalid = False


# more input validation
while invalid == True:
    print("wrong input")
    wdtwtd = input("yes or no? ")
    if wdtwtd == "chest" or wdtwtd == "door":
        invalid = False
    else:
        continue
if wdtwtd == "chest":
    print("you walk over to the chest and open it ")
    smcr = randint(1, 9)
    smc = items[smcr]
    punch = 1
    print(smc)
    if smc == "a sword" or smc == "an axe" or smc == "a spear" or smc == "a mace":
        weaponsslot = smc
        if punch == 1:
            punch = punch + 4
        elif punch != 1:
            punch = punch + 5
        print(f" you do {punch} damge now")
        print("you walk over to the door its locked")
elif wdtwtd == "door":
    print("you walk over to the door its locked")
doorfight()
print("complete ")