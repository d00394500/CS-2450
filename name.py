import random
print("Hello! I am going to try to guess your age")
name=input("What is your name? ")
game=True
win=False
min_guess=15
max_guess=40
first_guess=30
guess=first_guess

def play():
    global guess, game, win, min_guess, max_guess
    
    
    print(f"\n{name}, I think you are {guess} years old!")
    correct=input("Is that your age? y/n ")
    if correct == "y":
        print(f"\nI win! You are {guess} years old, {name}")
        game=False
        win=True
    elif correct == "n":
        high_low=input("Oh, is your age higher or lower? h/l ")
        if high_low=="h":
            min_guess=guess
            guess=(max_guess-guess)//2+guess
        elif high_low=="l":
            max_guess=guess
            guess=(min_guess+guess)//2
        else:
            print("PLEASE ONLY USE h OR l")
            return high_low
    else:
        print("\nPLEASE ONLY USE y OR n")
        return correct


while game:
    play()
