# number guesse

import random



score = 0
cat_score = 0

while True:



    print("choose a number 0-10!")
    user_action = int(input())
    computer_action = random.randint(0, 10)
    print("cat chose", computer_action)
    if user_action == computer_action:
        print("well done. cat exploded")
        score = score + 1
    else:
        if user_action < computer_action:
            print("Too low,")
        elif user_action > computer_action:
            print("Too high,")
        print("wrong. u exploded.")
        cat_score = cat_score + 1



    print("Your score:", score)
    print("cat score:", cat_score)
    play_again = input("Play again?: ")
    if play_again.lower() != "yes":
        break

play_again == "no"
False
play_again != "yes"
True
