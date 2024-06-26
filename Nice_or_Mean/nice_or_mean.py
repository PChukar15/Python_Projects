#
# Python: 3.12
#
# Author: Emmett J Espinosa
#
# Purpose: The Tech Academy - Python Course, creating first program.
#

def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean,")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation, Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    print("\n{}, your current total is : \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print("\nNice Job {}, you win! \nYour not an asshole!".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print("\n{} you were a bit of an asshole, \nso you lost!".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (y/n):\n>>>: ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nThank you for playing, {}!".format(name))
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)





if __name__ == '__main__':
    start()