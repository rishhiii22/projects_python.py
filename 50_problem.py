# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file'Hi-score.txt' which is either blank or contains the previous Hi-score.
#  You need to write a program to update the Hi-score whenever the game() function breaks the HI-score.

import random

def game():
    print("You are playing the game..")
    score = random.randint (1 , 99)
    #Fetch the hiScore
    with open("hiScore.txt") as f:
        hiScore = f.read()
        if(hiScore!=""):
         hiScore = int(hiScore)
        else:
           hiScore = 0

    print(f"Your score: {score}")
    if(score>hiScore):
        
        # Write this hiScore to the file
        with open("hiScore.txt" , "w") as f:
           f.write(str(score))


        return score

game()


