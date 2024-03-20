
import random

while True:
    user_action = input("roll dice?")
    possible_action = ["yes", "no"]
    if user_action == "no":
        print("well.. ok then *explodes*")
    elif user_action == "yes":
        print("*spins*... you got,",random.randint(0, 10))
    else:
        print("spell!!!!!")
    play_again = input("more?: ")
    if play_again.lower() != "yes":
        break
play_again == "no"
False
play_again != "yes"
True
