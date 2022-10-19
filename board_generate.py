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



            board_row.append(num)
            num_list.remove(num)

        board.append(board_row.copy())
        board_row.clear()
    return board


def random_num():

    board = []
    board_row = []
    counter = 0
    for index_column in range(0, 9):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for index_row in range(0, 9):
            num = random.choice(num_list)
            temp_num = num_list.copy()
            y = len(board)
            while y != 0:
                print(y)
                y -= 1
                while num == board[y][index_row]:
                    counter += 1
                    num = random.choice(num_list)



            board_row.append(num)
            num_list.remove(num)

        board.append(board_row.copy())
        board_row.clear()
    print(board)
    print(counter)



text = f''
board_size = 9
box_size = board_size / 3
#draw_board(board_size, box_size, text)
random_num()