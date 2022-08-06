import random, sys

print("Welcome to Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0

while True:
    print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit')
        playerMove = input.lower()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('Please ')