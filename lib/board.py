import random


class Board:

    def __init__(self, param=None):
        if param:
            self.from_list(param)
        else:
            self.board_array = []
            numbers_array = list(range(9))
            random.shuffle(numbers_array)
            self.from_list(numbers_array)

    def __str__(self):
        result = ""
        for i in range(3):
            result = result + str(self.board_array[i]) + '\n'
        return result

    def __eq__(self, other):
        return self.board_array == other.get_board()

    def __hash__(self):
        result = ""
        for i in range(3):
            result += "".join(str(x) for x in self.board_array[i])
        return int(result)

    def get_coords(self):
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == 0:
                    return i, j

    def get_board(self):
        return self.board_array

    def from_list(self, array):
        self.board_array = list(range(3))
        for i in range(3):
            self.board_array[i] = array[i * 3:((i + 1) * 3)]
