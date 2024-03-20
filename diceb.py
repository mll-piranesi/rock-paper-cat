echo "# rock-paper-cat" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/me11yc4t/rock-paper-cat.git
git push -u origin main


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
