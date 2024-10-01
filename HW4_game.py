# Emmalyn Holmquist
#CPSC 507
# HW 4
## This program runs a simulation of the game Let's Make a Deal!

import time
import random

#initializing variables & array
accumulated_prizes = []
round_num = 0
prize = ""
notprize = ""
prize_door = ""
unprize_door = ""
response = ""
response2 = ""
response3 = ""

# changes speed at which lines are printed
def print_lines(list):
    for i in list:
        print(i, flush=True)
        if len(i) < 70:
            time.sleep(2)
        else:
            time.sleep(3)

# introduction to game!
def intro():
    global prize
    global notprize
    #prize options and bad prize options
    prize = random.choice(["car", "vacation", "semester of your tuition paid", "million dollars", "free ticket to Notre Dame Football"])
    notprize = random.choice(["goat", "piece of chewed gum", "car that doesn't work", "pig", "hungry snake"])
    story = [
        "Welcome to Let's Make a Deal!",
        "In this game there are three items hidden behind three doors.",
        "There is one good prize and two bad prizes.",
        f"Currently, one door has a {prize}, one door has a {notprize}, and the last door has another {notprize}.",
        "Choose a door, and may the odds be in your favor!"]
    print_lines(story) # prints lines slowly

# First choice of doors
def choice_1():
   # global response
    response = str(input("Please pick 1, 2, or 3 to indicate which door you would like to select: \n"))
    return response

# Player decides to open door 1; reveal another door based on where prize is (will never reveal the door with the prize!)
def door_1():
    global prize_door
    global notprize
    prize_door = random.choice(["1", "2", "3"]) #chooses where prize is
    if prize_door == "1":
        unprize_door = random.choice(["2", "3"])
        dialogue1 = ["You have chosen door 1", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "2":
        unprize_door = "3"
        dialogue1 = ["You have chosen door 1", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "3":
        unprize_door = "2"
        dialogue1 = ["You have chosen door 1", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)


# Player decides to open door 2; reveal another door based on where prize is (will never reveal the door with the prize!)
def door_2():
    global prize_door
    prize_door = random.choice(["1", "2", "3"]) #chooses where prize is
    if prize_door == "1":
        unprize_door = "3"
        dialogue1 = ["You have chosen door 2", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "2":
        unprize_door = random.choice(["1", "3"])
        dialogue1 = ["You have chosen door 2", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "3":
        unprize_door = "1"
        dialogue1 = ["You have chosen door 2", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)


# Player decides to open door 3; reveal another door based on where prize is (will never reveal the door with the prize!)
def door_3():
    global prize_door
    prize_door = random.choice(["1", "2", "3"]) #chooses where prize is
    if prize_door == "1":
        unprize_door = "2"
        dialogue1 = ["You have chosen door 3", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "2":
        unprize_door = "1"
        dialogue1 = ["You have chosen door 3", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)

    elif prize_door == "3":
        unprize_door = random.choice(["1", "2"])
        dialogue1 = ["You have chosen door 3", "Before I reveal your prize, I will reveal another door.",
                     f"Behind door {unprize_door}, was a {notprize}."]
        print_lines(dialogue1)


# If player chooses to switch doors:
def switch():
    global round_num
    global prize
    round_num += 1 #count round numbers for concatenation statement of prizes at end
    if response == "1":
        if prize_door == "1":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize #setting prize to notprize is for later when we display the prize as a concatenated array
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

    elif response == "2":
        if prize_door == "1":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

    elif response == "3":
        if prize_door == "1":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen to switch doors.", "I will now open the last door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

    accumulation() #display round numbers thus far and the prizes won

# Player chooses not to switch doors:
def notswitch():
    global round_num
    global prize
    round_num += 1 #count round numbers for concatenation statement of prizes at end
    if response == "1":
        if prize_door == "1":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize #this is for displaying what the player won at the end
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

    elif response == "2":
        if prize_door == "1":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

    elif response == "3":
        if prize_door == "1":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

        elif prize_door == "2":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Oh no! Unfortunately you opened a door with a bad prize and won a {notprize}.",
                         "Better luck next time!"]
            prize = notprize
            print_lines(dialogue2)

        elif prize_door == "3":
            dialogue2 = ["You have chosen not to switch doors.", "I will now open your originally selected door and reveal your prize.",
                         f"Lucky you! You chose a door with a good prize and won a {prize}."]
            print_lines(dialogue2)
    accumulation() #display round numbers thus far and prizes

#choice to switch doors
def choice_2():
    global response2
    dialogue3 = ["Based on this new information, you may want to switch doors.", "I will give you one chance to switch."]
    print_lines(dialogue3)
    response2 = str(input("Would you like to switch doors? Type y for yes or n for no: \n").lower())
    return response2

#display accumulated prizes/not prizes
def accumulation():
    global round_num
    global accumulated_prizes
    print("Here is a summary of your winnings so far: ")
    accumulated_prizes.append("Round " +str(round_num)+ ": " + str(prize))
    print(accumulated_prizes)

# play again?

def play_again():
    print_lines(["Congratulations on your winnings.", "Would you like to play again?"])
    response3 = str(input("Please enter y for yes and n for no.\n").lower())
    if response3 == "y":
        lets_make_a_deal()
    elif response3 == "n":
        print("Thanks for playing!")
        exit()
    else:
        play_again()


# Game play
def game_pt1():
    global response

    response = choice_1() # Choose a door

    if response == "1":
        door_1()
    elif response == "2":
        door_2()
    elif response == "3":
        door_3()
    else:
        game_pt1()

def game_pt2():
    global response2

    response2 = choice_2() # Would you like to switch doors?

    if response2 == "y":
        switch() # will reveal your prize for if you switch doors
    elif response2 == "n":
        notswitch() #reveals prize if you do not switch doors
    else:
        game_pt2()



# Let's Make a Deal Game
def lets_make_a_deal():
    intro()
    game_pt1()
    game_pt2()
    play_again()


lets_make_a_deal()