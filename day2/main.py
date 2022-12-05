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
 
score = 0
with open('input.txt', 'r') as gameset:
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
        
    # print final score based on recommandations
    print(f'Final score: {score}')