board = {'1-1': '   ', '1-2': '   ', '1-3': '   ',
         '2-1': '   ', '2-2': '   ', '2-3': '   ',
         '3-1': '   ', '3-2': '   ', '3-3': '   ',
         }
win_comb = {'1': {'1-1', '1-2', '1-3'},
            '2': {'2-1', '2-2', '2-3'},
            '3': {'3-1', '3-2', '3-3'},
            '4': {'1-1', '2-1', '3-1'},
            '5': {'1-2', '2-2', '3-2'},
            '6': {'1-3', '2-3', '3-3'},
            '7': {'1-1', '2-2', '3-3'},
            '8': {'3-1', '2-2', '1-3'},
            }

def print_board(board):
    print(board['1-1'] + '|' + board['1-2'] + '|' + board['1-3'])
    print('---+---+---')
    print(board['2-1'] + '|' + board['2-2'] + '|' + board['2-3'])
    print('---+---+---')
    print(board['3-1'] + '|' + board['3-2'] + '|' + board['3-3'])
    
def win_player(board, turn):
    player_set = set()
    for k, v in board.items():
        if v == turn:
            player_set.add(k)

    for k, v in win_comb.items():
        if v <= player_set:
            return True
            break
    return False

turn = ' X '
player = None
for i in range(9):
    print_board(board)
    print(f'В какое поле поставить {turn}?')
    move = input('Введите значение от 1-1 до 3-3: ')
    board[move] = turn
    if win_player(board, turn):
        player = turn
        print(f'Поздравляем! Игрок {turn} выиграл ;)')
        break

    if turn == ' X ':
        turn = ' O '
    else:
        turn = ' X '
if player == None:
    print('Игра закончилась в ничью ;)')
print_board(board)
