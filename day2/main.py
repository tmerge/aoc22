from enum import Enum
## Player 1
# A = Rock (1)
# B = Paper (2)
# C = Scissor (3)

## Player 2
# X = Rock (1)
# Y = Paper (2)
# Z = Scissor (3)

# Win = 6
# Draw = 3
# Loose = 0

class GAMESHAPES(Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

def playNormal(gameset):
    score = 0
    for game in gameset:
        game = game.split()
        
        # check for win and add bonus based of shape
        if game[0] == 'A' and game[1] ==  'Y' or game[0] == 'B' and game[1] == 'Z' or game[0] == 'C' and game[1] == 'X':
            score += 6 # win bonus
            if  game[1] == 'X':
                score += 1
            elif game[1] == 'Y':
                score += 2
            elif game[1] == 'Z':
                score += 3
        # check for draw and add bonus based of shape
        elif game[0] == 'B' and game[1] == 'Y' or game[0] == 'A' and game[1] == 'X' or game[0] == 'C' and game[1] == 'Z':
            score += 3
            if game[1] == 'X':
                score += 1
            elif game[1] == 'Y':
                score += 2
            elif game[1] == 'Z':
                score += 3
        # check in case of loose what was choosed to play the game
        else:
            if game[1] == 'X':
                score += 1
            elif game[1] == 'Y':
                score += 2
            elif game[1] == 'Z':
                score += 3
    return score
    
def playGuided(gameset):
    score = 0
    for game in gameset:
        game = game.split()

        # check for case you should loose
        if game[1] == 'X':
            if game[0] == 'A':
                score += 3
            elif game[0] == 'B':
                score += 1
            elif game[0] == 'C':
                score += 2

        # check for case you should get a draw
        elif game[1] == 'Y':
            score += 3
            if game[0] == 'A':
                score += 1
            elif game[0] == 'B':
                score += 2
            elif game[0] == 'C':
                score += 3

        # check the case you should win
        elif game[1] == 'Z':
            score += 6
            if game[0] == 'A':
                score += 2
            elif game[0] == 'B':
                score += 3
            elif game[0] == 'C':
                score += 1 
    return score

with open('input.txt', 'r') as gameset:
    #nscore = playNormal(gameset)    
    gscore = playGuided(gameset)
    # print final score based on recommandations
    #print(f'Final nscore: {nscore}')

    # print finaö score based on guide 
    print(f'Final gscore: {gscore}')