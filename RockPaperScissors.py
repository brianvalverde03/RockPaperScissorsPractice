import random, sys, os


wins = 0
losses = 0
ties = 0

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
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
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
    print('*  To play you much chose either    *')
    print('*  rock, paper or scissors.         *')
    print('*  You win when you have won two    *')
    print('*  out of three.                    *')
    print('*************************************')
    title_screen_selections()



title_screen()