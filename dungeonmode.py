# import statements
from rn import randomenenimetotal
from Items import dungeonchestone

# declaring variables
skeletonhealth = 10
punch = 1
playerhealth = 20

# level 1
# starting story
print("everything around you turns to dust ")
print("you are now in an dungeon")
print("a skeleton shoots you ")
print("you lose 2 health")

# player damage
playerhealth = playerhealth - 2

# initiating attack loop
while skeletonhealth > 0:

    # asking if user wants to attack
    ptd = input("do you want to attack? ")
    
    # input validation
    if ptd == "yes" or ptd == "no" or ptd == "ptd":
        invalid = False
    else:
        continue

    # more input validation
    while invalid == True:
        print("wrong input")
        ptd = input("yes or no?")
        if ptd == "yes" or ptd == "no" or ptd == "ptd":
            invalid = False
        else:
            continue

    # if statement
    # if user says no, player damage
    if ptd == "no":
        print("You lose 2 health")
        # player damage
        playerhealth = playerhealth - 2
        # if user uses cheat codes skelly death
    if ptd == "ptd":
        # skelly death
        skeletonhealth = skeletonhealth - 10
        # if user days yes you commit murder slowly
    elif ptd == "yes":
        skeletonhealth = skeletonhealth - punch
        print(f"you did {punch} damage")

print("a door opens behind you ")
print("you walk through it two skeletons appear ")

totalenenemies = randomenenimetotal
while totalenenemies > 0:
    attackback = input("what do you want to do ")
    if attackback == "attack":
        invalid = False

    while invalid == True:
        print("wrong input")
        attackback = input("what do you want to do ")
        if attackback == "attack":
            invalid = False
        else:
            continue

    if attackback == "attack":
        print("attack 1 or 2")
        if attackback == 1:
            while skeletonhealth > 0:
                ptd = input("do you want to attack? ")
                if ptd == "no" or ptd == "yes" or ptd == "ptd":
                    invalid = False

                while invalid == True:
                    print("wrong input")
                    ptd = input("yes or no?")
                    if ptd == "yes" or ptd == "no" or ptd == "ptd":
                        invalid = False
                    else:
                        continue

                if ptd == "no":
                    print("You lose 2 health")
                    playerhealth = playerhealth - 2
                if ptd == "ptd":
                    skeletonhealth = skeletonhealth - 10
                elif ptd == "yes":
                    skeletonhealth = skeletonhealth - punch
                    print(f"you did {punch} damage")

        elif attackback == 2:
            while skeletonhealth > 0:
                ptd = input("do you want to attack? ")

                if ptd == "yes" or ptd == "no" or ptd == "ptd":
                    invalid = False

                while invalid == True:
                    print("wrong input")
                    ptd = input("do you want to attack")
                    if ptd == "yes" or ptd == "no" or ptd == "ptd":
                        invalid = False
                    else:
                        continue

                if ptd == "no":
                    print("You lose 2 health")
                    playerhealth = playerhealth - 2
                if ptd == "ptd":
                    skeletonhealth = skeletonhealth - 10
                elif ptd == "yes":
                    skeletonhealth = skeletonhealth - punch
                    print(f"you did {punch} damage")

    skeletonhealth = 10

lor = input("left or right?")

if lor == "left" or lor == "right":
    invalid = False

while invalid == True:
    print("wrong input")
    lor = input("left or right?")
    if lor == "left" or lor == "right":
        invalid = False
    else:
        continue
if lor == "left":
    print("you go left there is a chest")
    openchest = input("do you want to open the chest?")
    if openchest == "yes" or lor == "no":
        invalid = False

    while invalid == True:
        print("wrong input")
        openchest = input("yes or no?")
        if openchest == "yes" or openchest == "no":
            invalid = False
        else:
            continue

    if openchest == "no":
        goright = input("do you want to go right?")
        if goright == "yes" or goright == "no":
            invalid = False

        while invalid == True:
            print("wrong input")
            goright = input("yes or no?")
            if goright == "yes" or goright == "no":
                invalid = False
            else:
                continue

        if goright == "yes":
            print("you go right")
        elif goright == "no":
            print("you pass out")
            exit()
    elif openchest == "yes":
        print(f"inside is {dungeonchestone}")
        if dungeonchestone == "sword" or "mace" or "axe" or "spear":
            punch = punch + 4
            print(f"you do {punch} damage now")
        goright = input("do you want to go right?")
        if goright == "yes" or goright == "no":
            invalid = False

        while invalid == True:
            print("wrong input")
            goright = input("yes or no?")
            if goright == "yes" or goright == "no":
                invalid = False
            else:
                continue

        if goright == "yes":
            print("you go right")
        elif goright == "no":
            print("you pass out")
            exit()

elif lor == "right":
    print("you go right")
    nextlevel = input("do you want to go to the next level?")
    if nextlevel == "yes" or nextlevel == "no":
        invalid = False

    while invalid == True:
        print("wrong input")
        nextlevel = input("yes or no?")
        if nextlevel == "yes" or nextlevel == "no":
            invalid = False
        else:
            continue

    if nextlevel == "no":
        print("fuck you")
        print("you go to the next level")
    elif nextlevel == "yes":
        print("you go to the next level")
        print(playerhealth)
        print(punch)

# you die jk level 2
print("a wild boss appears ")

bossl1health = 25
# you die jk that's up to the user
# initiating attack loop
while skeletonhealth > 0:

    # asking if user wants to attack
    ptd = input("do you want to attack? ")
    # input validation
    if ptd == "yes" or ptd == "no" or ptd == "ptd":
        invalid = False

    # more input validation
    while invalid == True:
        print("wrong input")
        ptd = input("yes or no?")
        if ptd == "yes" or ptd == "no" or ptd == "ptd":
            invalid = False
        else:
            continue

    # if statement
    # if user says no, player damage
    if ptd == "no":
        print("You lose 2 health")
        # player damage
        playerhealth = playerhealth - 2
        # if user uses cheat codes skelly death
    if ptd == "ptd":
        # skelly death
        bossl1health = bossl1health - 10
        # if user days yes you commit murder slowly very slowly depending on how much damage you do
    elif ptd == "yes":
        bossl1health = bossl1health - punch
        print(f"you did {punch} damage")
# how dare you I spent no time at all on that boss, and you just kill him I don't care
print("you killed it ")
# to be continued
