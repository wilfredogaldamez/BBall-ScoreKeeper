import instructions

"""
Hello, this program will simulate an NBA game counter to keep track of statistics in an NBA game, mainly that of the
points. In other words, it is to be used by NBA fans looking to keep track or the NBA itself looking to maintain a live
record of statistics
"""

# Requests name from user
name = input('Welcome, please enter your name: \n')

# Greets user by name
introMessage = ('\nHi, ' + name + '! Nice to meet you.')
print(introMessage)

# Requesting decision from user to start game, view instructions, or to quit. Loops runs until user inputs 'q' for quit
while True:
    instruction = instructions.waiting_on_user()

    if instruction == instructions.instructionList[0]:
        instructions.start_game()

    elif instruction == instructions.instructionList[1]:
        instructions.send_instructions()

    elif instruction == instructions.instructionList[2]:
        instruction = instructions.quit_program()
        break

    elif instruction == instructions.instructionList[3]:
        instructions.clear_screen()
