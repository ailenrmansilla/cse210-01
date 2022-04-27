# Ailen Mansilla CSE 210 - 01 Week 2

from pyparsing import empty


line1 = [1,2,3]
line2 = [4,5,6]
line3 = [7,8,9]

def main():
    counter = 0
    empty = empty_squares()
    print_board(0,'X')
    winner = 0
    if counter%2 == 0:
        player = 'X'
    else:
        player='Y'
    while empty >= 1 or winner != 'X' or winner !='Y':
        print(f'----- Player \'{player}\' turn -----')
        square_number = int(input('Choose a square to mark (1-9): '))
        counter += 1
        while square_number > 9 or square_number < 1:
            square_number = int(input('Please, choose an empty square to mark (choose a number between 1-9): '))
        print_board(square_number,player)
        if counter%2 == 0:
            player = 'X'
        else:
            player='Y'
        empty = empty_squares()
        winner = find_winner()
        if winner == 'X' or winner=='Y':
            print(f'----{winner} WIN----')
            break
        elif winner == 0 and empty == 0:
            print('---Tie---\n---There was not a winner---')
            break

        

def print_board(square_number,player):
    if square_number !=0:
        if square_number in line1:
            line1[square_number-1] = player
        elif square_number in line2:
            line2[square_number-4] = player
        elif square_number in line3:
            line3[square_number-7] = player

    print(f'___ ___ ___')
    print(f'| {line1[0]} | {line1[1]} | {line1[2]} |')
    print(f'___ ___ ___')
    print(f'| {line2[0]} | {line2[1]} | {line2[2]} |')
    print(f'___ ___ ___')
    print(f'| {line3[0]} | {line3[1]} | {line3[2]} |')
    print(f'___ ___ ___')
    
    
def find_winner():
    if line1[0] == line1[1] and line1[1] == line1[2]:
        return line1[0]
    elif line2[0] == line2[1] and line2[1] == line2[2]:
        return line2[0]
    elif line3[0] == line3[1] and line3[1] == line3[2]:
        return line3[0]
    elif line1[0] == line2[0] and line3[0] == line2[0]:
        return line1[0]
    elif line1[1] == line2[1] and line3[1] == line2[1]:
        return line1[1]
    elif line1[2] == line2[2] and line3[2] == line2[2]:
        return line1[2]
    elif line1[0] == line2[1] and line3[2] == line2[1]:
        return line1[0]
    elif line1[2] == line2[1] and line3[0] == line2[1]:
        return line1[2]
    else:
        return 0


def empty_squares():
    empty = 9
    for i in range(0,2):
        if 'X' == line1[i] or 'Y' == line1[i]:
            empty -= 1
        if 'X' == line2[i] or 'Y' == line2[i]:
            empty -= 1
        if 'X' == line3[i] or 'Y' == line3[i]:
            empty -= 1
    return empty

if __name__ =="__main__":
    main()
