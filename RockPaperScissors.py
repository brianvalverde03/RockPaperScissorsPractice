import random, sys, os


wins = 0
losses = 0
ties = 0
playerMove = ''
computerMove = ''

def title_screen_selections():
    option = input('> ')
    if option.lower() == ("play") or option.lower() == ("p"):
        start_game()
    elif option.lower() == ("help") or option.lower() == ("h"):
        help_menu()
    elif option.lower() == ("quit") or option.lower() == ("q"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command.')
        if option.lower() == ("play") or option.lower() == ("p"):
            start_game()
        elif option.lower() == ("help") or option.lower() == ("h"):
            help_menu()
        elif option.lower() == ("quit") or option.lower() == ("q"):
            sys.exit()

def title_screen():
    os.system('cls')
    print('*************************************')
    print('* Welcome to Rock, Paper, Scissors! *')
    print('*            - Play -               *')
    print('*            - Help -               *')
    print('*            - Quit -               *')
    print('*************************************')
    title_screen_selections()

def help_menu():
    os.system('cls')
    print('*************************************')
    print('* Welcome to Rock, Paper, Scissors! *')
    print('*************************************')
    print('*  To play you must chose either    *')
    print('*  rock, paper or scissors.         *')
    print('*  You win when you have won two    *')
    print('*  out of three.                    *')
    print('*************************************')
    title_screen_selections()

def players_choice():
    playerMove = input()
    if playerMove.lower() == 'r':
        print('Rock versus...')
        cpu_response()
    elif playerMove.lower() == 'p':
        print('Paper versus...')
        cpu_response()
    elif playerMove.lower() == 's':
        print('Scissors versus...')
        cpu_response()
    while playerMove.lower() not in ['r', 'p', 's']:
        print('Please enter a valid command.')
        playerMove = input.lower('> ')
        if playerMove.lower() == 'r':
            print('Rock versus...')
            cpu_response()
        elif playerMove.lower() == 'p':
            print('Paper versus...')
            cpu_response()
        elif playerMove.lower() == 's':
            print('Scissors versus...')
            cpu_response()

def cpu_response():
    randomNum = random.randint(1,3)
    if randomNum == 1:
        print('Rock')
        game_result()
    elif randomNum == 2:
        computerMove = 'p'
        print('Paper')
        game_result()
    elif randomNum == 3:
        computerMove = 's'
        print('Scissors')
        game_result()

def game_result():
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1
        print('{}s Wins, {}s Losses, {}s Ties'.format(wins, losses, ties))

def start_game():
    print('Please choose your move: rock(1), paper(2), scissors(3)')
    players_choice()


title_screen()