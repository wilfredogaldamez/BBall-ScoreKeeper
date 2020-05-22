from os import system, name
import time


class Instructions:
    pass


instructionList = ['p', 'i', 'q', 'c']
userInputMessage = 'Enter p to play, i for instruction, q to quit or c to clear the screen: \n'
tryAgainMessage = '\nPlease type a valid command.\n' + userInputMessage
quitGameMessage = '\nBye. Thanks for playing!'
gameInstructionsMessage = """
When the game starts:
If team Lebron scores, press l. If team Kobe scores, press k. 
Once the game is final, press f. 
The winning team and its score will be displayed. 
"""
whoScoredMessage = 'Press k if team Kobe scores, l if team Lebron scores and f for the final score...\n'
tryAgainWhoScoredMessage = tryAgainMessage + whoScoredMessage
lebronTeamWins = '\nFinal Score: Team Lebron has won with: '
kobeTeamWins = '\nFinal Score: Team Lebron has won with: '
tie = 'The game was drawn at: '


def waiting_on_user():
    user_input = input(userInputMessage).lower()
    while user_input not in instructionList:
        user_input = input(tryAgainMessage).lower()
    return user_input


def start_game():
    lebron_team = 0
    kobe_team = 0
    game_start_flag = True

    while True:
        clear_screen()
        if game_start_flag:
            print('The game has started!')
        user_input = input(whoScoredMessage).lower()
        if user_input == 'l':
            lebron_team += 1
        elif user_input == 'k':
            kobe_team +=1
        elif user_input == 'f':
            break
        else:
            print(tryAgainWhoScoredMessage)
        game_start_flag = False

    if lebron_team > kobe_team:
        print(lebronTeamWins + str(lebron_team) + '\n')
    elif kobe_team > lebron_team:
        print(kobeTeamWins + str(kobe_team) + '\n')
    else:
        print(tie + str(kobe_team) + '\n')


def send_instructions():
    print(gameInstructionsMessage)


def quit_program():
    print(quitGameMessage)


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')