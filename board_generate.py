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
    for index_column in range(0, 9):
        for index_row in range(0, 9):
            board_row.append(random.randint(1, 9))
        board.append(board_row.copy())
        board_row.clear()
    return board


def random_num():
    list_test = []
    counter = 0
    for i in range(0, 9):
        num = random.randint(1, 9)
        counter += 1
        while num in list_test:
            num = random.randint(1, 9)
            counter += 1
        list_test.append(num)
    print(list_test)
    print(counter)



text = f''
board_size = 9
box_size = board_size / 3
#draw_board(board_size, box_size, text)
random_num()