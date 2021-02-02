# name: Breann Nielsen
# date: 12/4/2020
# description: text-based adventure game

# Global imports
import random
import sys
import time

def print1by1(text, delay=0.0001):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

def displayIntro():
    time.sleep(1)
    print1by1("It has been many years since the vault was sealed...")
    time.sleep(2)
    print1by1(" Since the bombs fell.")
    time.sleep(2)
    print1by1(" You wake up in a disoriented state, seemingly trapped within a windowed coffin.")
    time.sleep(2)
    print()
    print1by1("How will you escape?")
    time.sleep(2)
    print()

def start_room():
    start_room_options = ["1","2","3"]
    action = ""
    while action not in start_room_options:
        print("You have three options. What would you like to do?: 1) inspect window, 2) inspect door latch, 3) inspect overhead wires.")
        action = str(input("Enter option number: "))
    print("You have selected " + action)
    if action == start_room_options[0]:
        incorrect01()
    elif action == start_room_options[1]:
        incorrect02()
    elif action == start_room_options[2]:
        correct01()

def incorrect01():
    print("It's a thick, solid glass. I don't think I can break that.")
    time.sleep(2)

def incorrect02():
    print("It's sealed tight. Won't budge.")
    time.sleep(2)

def correct01():
    str(input("These wires might do something. Should I pull on them? Y/N"))
    time.sleep(2)


#     print("You inspect the door latch.")
#     time.sleep(2)
#     print("It's sealed tight. Won't budge.")

#     correctAction = "inspect overhead wires"

#     if chosenAction == str(correctAction):
#         print("These wires might do something. Should I pull on them?")

# Main program
displayIntro()
start_room()