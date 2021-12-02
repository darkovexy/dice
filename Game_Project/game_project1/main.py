# Snake,water and gun game
from math import trunc
import random

def gameWin(ply1,ply2):
    if ply1 == ply2:
        return None
    if ply1 == "s":
        if ply2 == "w":
            return False
        elif ply2 == "g":
            return True
    if ply1 == "w":
        if ply2 == "s":
            return True
        elif ply2 == "g":
            return False
    if ply1 == "g":
        if ply2 == "w" :
            return True
        elif ply2 == "s":
            return False

print("Welcome to Snake,Water and Gun game-------\n")
randNo = random.randint(1,3)
comp = print("Computer turn: press snake(s) or water(w) or gun(g)")
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
else:
    comp = "g"

you = input("your turn: Press snake(s) or water(w) or gun(g) : \n")
print(f"computer chose {comp}\n")
print(f"You choose {you} \n")
winner = gameWin(comp,you)
if winner == None:
    print("Tie!!")
elif winner == False:
    print("Computer win!")
else :
    print("You win!")