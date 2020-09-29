# File:          proj1.py
# Author:        Kai Vilbig
# Date:          10/18/2018
# Section:       28
# E-mail:        sw92057@umbc.edu
# Description:   This program is a text-based adventure game. The premise
#                of this game is that you went camping in the woods only
#                to find out that a monster, The Demogorgon, was set loose
#                from the lab conveniently located in the same forest. The
#                object of this game is to run away from that monster. If
#                you can stay alive for seven days, or if you travel 150
#                miles to the nearest big city, then you win the game. If
#                you die at the hands of the monster, or by some other
#                means, you lose the game.

from random import randint, seed
seed(100)

MAX_HEALTH = 100
MIN_HEALTH = 0
MAX_DEM_HEALTH = 300
DEM_ATTACK = 20

SURVIVE_DAYS = 7
SURVIVE_DIST = 150

FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]

ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]

ITEMS_NOT_EQUIPABLE = ["Bicycle", "Hi-C", "Heelys", "Walkman"]

ITEM_EFFECT_DESCR = ["is an equipable weapon.", \
                     "improves your distance travelled.", \
                     "halves The Demogorgon's health at the start of a fight.", \
                     "improves your distance travelled.", \
                     "decreases The Demogorgon's attack by 25%.", \
                     "is an equipable weapon.", "is an equipable weapon."]

# these are just values because they will be multiplied by the needed
# values leter
ITEM_EFFECT = [5, 10, 50, 1.5, .5, 1.25, .75, 100, 25]

# by passing in the list to print out, the code to print doesnt
# have to be repeated
def printOptions(options):

    # goes through each item and prints them out on separate lines
    print("Your options are:")
    loop = 0
    while loop < len(options):
        print(options[loop])
        loop += 1

# Equipts or unequipts items
def equiptItem(items, itemEquipped):

    print()
    options = ["1 - Equipt", "2 - Unequipt", "3 - I Changed my mind"]
    printOptions(options)
    
    choice = int(input("Enter a choice: "))
    print()

    # creates a list of items that the user can equipt
    itemOptions = []
    loop = 0

    # adds items from the list passed in to itemOptions
    while loop < len(items):
        if items[loop] not in ITEMS_NOT_EQUIPABLE:
            item = str(loop + 1) + " - " + str(items[loop])
            itemOptions.append(item)
        loop += 1
    
    if choice == 1:
        
        printOptions(itemOptions)

        whichItem = int(input("Enter a choice: "))

        # set itemNo to 1 less than the user input to get location in list
        # of the chosen item
        itemNo = whichItem - 1

        # since item in the list has "1 - " infront of it, this splits the item
        # into the number, the dash and the item so that we can equipt only the item.
        # we can get only the item by getting the 3rd index in the list
        holdItem = itemOptions[itemNo].split()

        if len(holdItem) > 3:
            holdItem[2] += " " + holdItem[3]
        
        print("You equipped", holdItem[2])
        return holdItem[2]

    # sets held item to "N/A"
    if choice == 2:
        holdItem = "N/A"
        return holdItem

    # nothing added to itemEquipped
    if choice == 3:
        holdItem = itemEquipped[0]
        return holdItem

# has the player chose what they want to do in the morning
def morningChoice(items, health, distance, itemEquipped, morningDone, first):

    # only prints what else the user wants to do if the user has already done something
    # in the morning
    if first != 0:
        print()
        print("What else do you want to do this morning?")
        print()
        
    options = ["1 - View Inventory", "2 - View Current Stats", \
               "3 - Eat an Eggo Waffle", "4 - Nothing else."]
    printOptions(options)

    choice = int(input("Enter a choice: "))
    print()

    # print inventory
    if choice == 1:
        print("Here is what your inventory looks like:")
        print(items)
        print()
        print("You can not equipt every item in your inventory")
        
        # call function to equipt or unequipt an item
        if len(items) != 0:
            itemEquipped[0] = equiptItem(items, itemEquipped)

    # print current stats
    elif choice == 2:
        print("Health:", health[0])
        print("Distance travelled:", distance)
        print("Equipped item:", itemEquipped[0])
        
    # eats an eggo waffle which increases player health by 10 points
    elif choice == 3:
        if health[0] < MAX_HEALTH:
            health[0] += 10

            # makes sure health doesnt exceed max health
            if health[0] > MAX_HEALTH:
                health[0] = MAX_HEALTH

        print("You ate the Eggo Waffle. So bad, yet so good.")
        print("Your health has increased by 10 points.")
        
    # changes morningDone to True which gets out of the morning loop
    # and the player can proceed to the next part of the day
    else:
        morningDone[0] = True

# fighting mechanic
def fight(items, health, itemEquipped):

    print()
    print("The Demogorgon appears in front of you.")
    print("Its face opens up like a flower to display rows and rows of " \
          "teeth. It came here for a fight.")

    fightList = ["1 - Fight", "2 - Flail", "3 - Flee"]
    demHealth = MAX_DEM_HEALTH
    fight = True

    while fight and health[0] > 0 and demHealth > 0:

        demAttack = DEM_ATTACK

        if "Hi-C" in items:
            demHealth *= 0.5

        if "Walkman" in items:
            demAttack *= 0.75

        print()
        print("Your health:", health[0])
        print("Monster health:", demHealth)
        print()
        print("What do you do now?")
        print()

        printOptions(fightList)
        choice = int(input("Enter a choice: "))

        # fight
        if choice == 1:
            if itemEquipped[0] == "Flashlight":
                print("You strike the Demogorgon with your", itemEquipped[0], \
                      "for 5 damage")
                demHealth -= 5

            elif itemEquipped[0] == "Walkie Talkie":
                print("You strike the Demogorgon with your", itemEquipped[0], \
                      "for 10 damage")
                demHealth -= 10
                
            elif itemEquipped[0] == "Rubber Band":
                print("You strike the Demogorgon with your", itemEquipped[0], \
                      "for 25 damage")
                demHealth -= 25
                
            elif itemEquipped[0] == "Sword":
                print("You strike the Demogorgon with your", itemEquipped[0], \
                      "for 50 damage")
                demHealth -= 50
                
            elif itemEquipped[0] == "Laser Cannon":
                print("You strike the Demogorgon with your", itemEquipped[0], \
                      "for 100 damage")
                demHealth -= 100
                
            else:

                print("You punched the Demogorgan with your fist like a bad @$$", \
                      "but it didn't do any damage")

            
            print("The Demogorgon strikes you back for", demAttack, "damage.")
            health[0] -= demAttack

        # flee
        elif choice == 3:
            fleeChance = randint(1,10)

            # flee successful
            if fleeChance <= 3:
                print("You try to run away from the fight. You are successful," \
                      " and you live to die another day.")
                fight = False
                    
            # flee unsuccessful
            else:
                print("You try to run away from the fight. The Demogorgon blocked" \
                      "your attempt to run.")

                demAttack *= .5
                print("It hits you for", demAttack, "damage.")
                
                health[0] -= demAttack

        if health[0] <= 0 or choice == 2:
            Fight = False
            health[0] = 0

            print()
            print("You died")

            
# randomly choses what event occurs
def event(health, items, day, itemEquipped):

    print()
    chance = randint(1,10)

    # 20% chance of finding food
    if chance <= 2:
        
        foodsHealth = [-30, -5, 15, 25, 30]
        options = ["1 - eat it", "2 - put it back"]
        
        # gets which food is found
        foodChance = randint(0,4)
        whichFood = FOODS[foodChance]
        foodHealth = foodsHealth[foodChance]

        print("As you were walking, you found a backpack.")
        print("Inside the backpack, there was some", whichFood)
        print()
        
        printOptions(options)
        choice = int(input("Enter a choice: "))

        # eat food and adjust health
        if choice == 1:
            print("You ate the", whichFood)
            health[0] += foodHealth

            if health[0] > MAX_HEALTH:
                health[0] = MAX_HEALTH
            
        else:
            print("You put the", whichFood, "back")
            print()
            
    # finds an item
    elif chance <= 4:

        whichItem = randint(0,6)
        print()
        print("You pass by and old shed and decide to go inside." \
              " Something on the shelf catches your eye.")
        print("You reach up to grab the item. It's a", ITEMS[whichItem] + ".")
        print()
        
        if ITEMS[whichItem] not in items:
            items.append(ITEMS[whichItem])
            print("The", ITEMS[whichItem], "has been added to your inventory.")
            print("The", ITEMS[whichItem], "you found", ITEM_EFFECT_DESCR[whichItem])

        else:
            print("You already have a", ITEMS[whichItem], "in your" \
                  " inventory so you put it back.")
            
    # fall into a ditch
    elif chance <= 6:
        print("You fell into a trench becuase you weren't paying" \
              " attention to where you were stepping.")
        print("It takes you a whole extra day to climb out.")
        
        day[0] += 1

    # fight
    elif chance <= 9:
        fight(items, health, itemEquipped)


# player moves
def move(health, distTravelled, items, day, itemEquipped):
    chance = randint(1,10)
    
    # 60% chance an event happens
    if chance <= 6:
        event(health, items, day, itemEquipped)
        

# player does not move
def stay(health, items, itemEquipped):
    chance = randint(1,10)

    #70% chance monster catches up and fights
    if chance <= 7:
        fight(items, health, itemEquipped)


# the user choses whether or not to move or stay for the day
def moveOrStay(health, distTravelled, items, day, itemEquipped):

    print("The Demogorgon looms in the distance." \
          " Do you leave your camp, or do you stay?")
    print()
    
    options = ["1 - Pack up camp and go", "2 - Stay where you are"]
    printOptions(options)

    choice = int(input("Enter a choice: "))
    print()

    # move
    if choice == 1:
        print("You quickly pack up your camp.")
        print("You begin heading in the direction of the nearest town.")

        move(health, distTravelled, items, day, itemEquipped)

    # stay
    if choice == 2:
        stay(health, items, itemEquipped)
        return False


# cahracter whips and nae naes if the player wins
def whipNaeNae():
    print()
    print("     ,,,,,,,            ,,,,,,,    ")
    print("    | >  O |      |||  | O  O |    ")
    print("    | ____ |        \  | ____ |    ")
    print("     ------          \  ------     ")
    print("     /| |\                | | \\   ")
    print(" ( )/ | | \__             | |  \__ ")
    print("    __   __              __  __    ")
    print("   /       \            /      \\  ")
    print("__/         \__      __/        \__")


# displays the players finl stats
def finalStats(health, distTravelled, itemEquipped):        

    print("Final Stats:")
    print()
    print("Health:", health[0])
    print("Distance travelled:", distTravelled)
    print("Equipped item:", itemEquipped[0])
    print()


# main function
def main():

    # by making some of the variables lists, the program
    # can update thevalues inside from within a different function
    health = [MAX_HEALTH]
    day = [1]
    distTravelled = 0
    items = ["Flashlight", "Walkie Talkie"]
    itemEquipped = ["N/A"]

    # Game beginning messages
    print()
    print("After miles and miles of hiking in the woods, you finally setup your camp.")
    print("You decided to go camping on the wrong weekend.")
    print("Your phone buzzes:")
    print("		THE DEMOGORGON HAS ESCAPED.		RUN.")
    
    while day[0] <= 7 and health[0] > 0 and distTravelled < 150:

        addDist = [True]

        # calculate the distance the player travels that day
        if "Bicycle" in items and addDist != False:
            distTravelled += (((health[0] / 4) + 5) * ITEM_EFFECT[3])
            print("The Bicycle in your inventory inmproved your distance travelled")

        elif "Heelys" in items and addDist != False:
            distTravelled += (((health[0] / 4) + 5) * ITEM_EFFECT[5])
            print("The Heelys in your inventory inmproved your distance travelled")

        elif addDist != False:
            distTravelled += ((health[0] / 4) + 5)

        print()
        print("The sun rises on Day", day[0], "in the forest.")
        print()
        print("What would you like to do this morning?")
        print()

        # set first to 0 so that the first time morningChoice is called, it will not
        # print "what else would you like to do this morning"
        first = 0
        morningDone = [False]
        while morningDone[0] != True:
   
            morningChoice(items, health, distTravelled, itemEquipped, morningDone, first)

            # Change first so that the next time we call morningChoice it will
            # print "what else would you like to do this morning"
            first = 1

        addDist[0] = moveOrStay(health, distTravelled, items, day, itemEquipped)
        
        # end of the day messages
        day[0] += 1
        print()
        print("You have now travelled", distTravelled, "miles")

    if health[0] > 0:
        if distTravelled >= 150:
            print("You made it out of the forest alive!")
        
        # in case you survive the 7th day only because you were climbing
        # out of a ditch and was not near civilization yet
        else:
            print("You survived 7 days.")
            print("A group of people trying to catch the monster found you " \
                  "and took you back to civilization")

        print("YOU WON!!")
        whipNaeNae()
        
        print()
        print("It took you", day[0] - 1, "days to travel", distTravelled, "miles.")
    print()

    finalStats(health, distTravelled, itemEquipped)

    
main()
