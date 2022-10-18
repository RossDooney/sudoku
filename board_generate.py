import random
import copy


def draw_board(size, box, text):
    board = create_random_board()
    for index_column in range(0, size):
        if index_column % box == 0:
            text += '\n--------------\n'
        else:
            text += '\n'
        for index_row in range(0, size):
            text += f'{board[index_column][index_row]}'
            if (index_row + 1) % 3 == 0:
                text += f'| '
    print(text)


def create_random_board():
    board = []
    board_row = []
    counter = 0
    for index_column in range(0, 9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for index_row in range(0, 9):
            num = random.choice(num_list)
            counter += 1
            while num in board_row:
                num = random.randint(1, 9)
                counter += 1
            board_row.append(num)
        board.append(board_row.copy())
        board_row.clear()
    return board, counter


def random_num():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board = []
    coun = 0
    for index_row in range(0, 9):
        num = random.choice(num_list)
        coun += 1
        board.append(num)
        num_list.remove(num)
    print(board)
    print(coun)



text = f''
board_size = 9
box_size = board_size / 3
#draw_board(board_size, box_size, text)
random_num()