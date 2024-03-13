board = {'1-1': '   ', '1-2': '   ', '1-3': '   ',
         '2-1': '   ', '2-2': '   ', '2-3': '   ',
         '3-1': '   ', '3-2': '   ', '3-3': '   ',
         }

def print_board(board):
    print(board['1-1'] + '|' + board['1-2'] + '|' + board['1-3'])
    print('---+---+---')
    print(board['2-1'] + '|' + board['2-2'] + '|' + board['2-3'])
    print('---+---+---')
    print(board['3-1'] + '|' + board['3-2'] + '|' + board['3-3'])
    
turn = ' X '
for i in range(9):
    print_board(board)
    print(f'В какое поле поставить {turn}?')
    move = input('Введите значение от 1-1 до 3-3: ')
    board[move] = turn
    if turn == ' X ':
        turn = ' O '
    else:
        turn = ' X '
print_board(board)