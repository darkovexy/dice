import random
randomNumbers = random.randint(1,100)

userGuesses = None
guesses = 0 

while userGuesses != randomNumbers:
    userGuesses = int(input("Enter the guess number: "))
    guesses += 1
    
    if userGuesses == randomNumbers:
        print("Great! YOu guess the number correctly.")
    else :
        if userGuesses > randomNumbers:
            print("You guess it wrong! Enter a lower number.")
        else:
            print("You guess it wrong! Enter a larger number.")

print(f"On the {guesses} no.of guesses you did it correctly.")
with open("Game_Project\game_project2\hiscore.txt", "r") as f:
    hiscore = int(f.read())
if guesses < hiscore:
    with open("Game_Project\game_project2\hiscore.txt", "w") as f:
        f.write(str(guesses)) 
