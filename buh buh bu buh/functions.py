from main import armourslot
from main import weaponsslot
from main import itemsslots
from Items import items
from random import randint


#inventory function
def inventory():
    print("armour ", armourslot)
    print("weapon ", weaponsslot)
    print("items ", itemsslots)

def inputvalidationchest():
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

def inputvalidationdoor():
    invalid = True
    if ptd == "yes" or ptd == "no" or ptd == "ptd":
        invalid = False


    # more input validation
    while invalid == True:
        print("wrong input")
        ptd = input("yes or no? ")
        if ptd == "yes" or ptd == "no" or ptd == "ptd":
            invalid = False
        elif ptd == "inventory":
            inventory()
            invalid = False
        else:
            continue

def inputvalidationlookaround():
    invalid = True
    if laatd == "yes" or laatd == "no":
        invalid = False
    elif laatd == "inventory":
        inventory()
        invalid = False

    # more input validation
    while invalid == True:
            print("wrong input")
            laatd = input("yes or no ")
            if laatd == "yes" or laatd == "no":
                invalid = False
            else:
                continue

#chest function
def chestfunction():
    chest = input("do you want to open the chest ")
    print("")

    inputvalidationchest()

    ranum = randint(0, 9)
    chestia = items[ranum]
    if chest == "no":
        print("you headbutt the chest")
        exit()
    elif chest == "yes":

        print(f"you open the chest inside is {chestia}")
        if chestia == "a sword" or chestia == "a mace" or chestia == "an axe" or chestia == "a spear":
            punch = punch + 4
            weponsslot = chestia
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

        elif chestia == "iron armour" or chestia == "leather armour" or chestia == "diamond armour":
            if chestia == "leather armour":
                armourlvl = armourlvl + 1
                armourslot = chestia
            elif chestia == "iron armour":
                armourlvl = armourlvl + 2
                armourslot = chestia
            elif chestia == "diamond armour":
                armourlvl = armourlvl + 3
                armourslot = chestia
