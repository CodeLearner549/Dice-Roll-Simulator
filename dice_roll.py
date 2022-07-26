# Dice Roll Simulator

import random

loop = True

randNum = random.randrange  # already function


def roll(a):
    for n in range(a):
        first = randNum(1, 7)  # arguements
        second = randNum(1, 7)
        total = first + second
        print(str(first) + "," + str(second) +
              " (" + "sum: " + str(total) + ")")


while loop:
    selection = input("""
    Dice Roll Simulator Menu
    1. Roll Dice Once
    2. Roll Dice 5 Times
    3. Roll Dice 'n' Times
    4. Roll Dice until Snake Eyes
    5. Exit
    Select and option (1-5)
    """)

    if selection == "1":
        roll(2)
    elif selection == "2":
        roll(5)
    elif selection == "3":
        number = input("How many rolls would you like? ")
        roll(int(number))
    elif selection == "4":
        tally = 0
        first = 0  # define before loop
        second = 0
        while first != 1 or second != 1:  # stays in loop when either of the two are not equal one
            first = randNum(1, 7)
            second = randNum(1, 7)
            total = first + second
            print(str(first) + "," + str(second) +
                  "(" + "sum: " + str(total) + ")")
            tally = tally + 1
        print("SNAKE EYES it took " + str(tally) + " rolls to get snake eyes.")
    elif selection == "5":
        exit()
