# ----- import -----
import os
from random import randint


# ----- def -----
def header():
    print('-' * 30)
    print('Noughts Crosses')
    print('-' * 30)


# ----- var -----
hashes = [[[], [], []], [[], [], []], [[], [], []]]

header()
option = int(input('1 - To "X"\n'      # Decide whether the player want 'X' or 'O' 
                   '2 - To "O"\n'
                   'Choice: '))
chance_hash = 0
games = 0
# ----- Check the option -----
if option == 1:
    option = 'X'
    option_machine = 'O'
else:
    option = 'O'
    option_machine = 'X'

# ----- Clean the screen -----
os.system('CLS')
while True:
    while True:
        os.system('CLS')
        header()
        machine = randint(0, 2)
        machine2 = randint(0, 2)

        # ----- HASH -----
        for i, n in enumerate(hashes):
            print(f'   {i+1:}', end='')
        print()
        for i, n in enumerate(hashes):
            print(f'{i+1}   {n}  ')

        # ----- Player! # Make sure whether the location where the player chooses is empty -----
        print('\nChoice a line and a column [1 till 3]\n')
        while True:
            line = str(input('Line: ')).strip()    # player chooses a line
            column = str(input('Column: ')).strip()  # player chooses a column
            if not line.isnumeric:         # make sure if the line is numeric
                print('please enter a valid value')
                continue

            if not column.isnumeric:        # make sure if the column is numeric
                print('please enter a valid value')
                continue

            line = int(line)
            column = int(column)

            if line > 3 or line < 1 and column > 3 or column < 1:
                print('please enter a valid value')
                continue
            else:
                break
        if option not in hashes[line-1][column-1] and option_machine not in hashes[line-1][column-1]:
            hashes[line - 1][column - 1].append(option)
        else:
            print('invalid option')
            continue

        #  ----- Condition to win -----
        if option in hashes[0][0] and option in hashes[1][0] and option in hashes[2][0]:  # Won in column 0 V
            print('You won!')
            break
        if option in hashes[0][1] and option in hashes[1][1] and option in hashes[2][1]:  # won in column 1 V
            print('You won!')
            break
        if option in hashes[0][2] and option in hashes[1][2] and option in hashes[2][2]:  # won in column 2 V
            print('You won!')
            break
        if option in hashes[0][0] and option in hashes[0][1] and option in hashes[0][2]:  # won in line 0 >>
            print('You won!')
            break
        if option in hashes[1][0] and option in hashes[1][1] and option in hashes[1][2]:  # won in line 1 >>
            print('You won!')
            break
        if option in hashes[2][0] and option in hashes[2][1] and option in hashes[2][2]:  # won in line 2 >>
            print('You won!')
            break
        if option in hashes[0][0] and option in hashes[1][1] and option in hashes[2][2]:  # won in diagonal >
            print('You won!')
            break
        if option in hashes[2][0] and option in hashes[1][1] and option in hashes[0][2]:  # won in diagonal <
            print('You won!')
            break

        # ----- Machine   # Make sure whether the location where the machine chooses is empty -----
        while True:
            machine = randint(0, 2)
            machine2 = randint(0, 2)
            if option_machine not in hashes[machine][machine2] and option not in hashes[machine][machine2]:
                hashes[machine][machine2].append(option_machine)
                break
            elif chance_hash == 10:
                print('DRAW!')
                break
            else:
                chance_hash += 1
                continue

        # ----- Condition to lose -----
        if option_machine in hashes[0][0] and option_machine in hashes[1][0] and option_machine in hashes[2][0]:   # lose in column 0 V
            print('You lose!')
            break
        if option_machine in hashes[0][1] and option_machine in hashes[1][1] and option_machine in hashes[2][1]:  # lose in column 1 V
            print('You lose!')
            break
        if option_machine in hashes[0][2] and option_machine in hashes[1][2] and option_machine in hashes[2][2]:  # lose in column 2 V
            print('You lose!')
            break
        if option_machine in hashes[0][0] and option_machine in hashes[0][1] and option_machine in hashes[0][2]:  # lose in line 0 >>
            print('You lose!')
            break
        if option_machine in hashes[1][0] and option_machine in hashes[1][1] and option_machine in hashes[1][2]:  # lose in line 1 >>
            print('You lose!')
            break
        if option_machine in hashes[2][0] and option_machine in hashes[2][1] and option_machine in hashes[2][2]:  # lose in line 2 >>
            print('You lose!')
            break
        if option_machine in hashes[0][0] and option_machine in hashes[1][1] and option_machine in hashes[2][2]:  # lose in diagonal >
            print('You lose!')
            break
        if option_machine in hashes[2][0] and option_machine in hashes[1][1] and option_machine in hashes[0][2]:  # lose in diagonal <
            print('You lose!')
            break

        # ----- check if all the options was chosen -----
        games += 2
        if games >= 9:
            break
    # ----- HASH -----
    for i, n in enumerate(hashes):
        print(f'   {i + 1:}', end='')
    print()
    for i, n in enumerate(hashes):
        print(f'{i + 1}   {n}  ')
    r = input('Want to play again? [S/N]').strip().upper()
    if r == 'N':
        break
    else:
        hashes.clear()
        games = 0
        hashes = [[[], [], []], [[], [], []], [[], [], []]]

input('Enter to Exit')
