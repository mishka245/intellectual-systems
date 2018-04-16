from lib.board import Board
from lib.my_queue import MyQueue

TARGET_STATE = Board([1, 2, 3, 4, 5, 6, 7, 8, 0])


def tree_search(problem, target):
    list_open = MyQueue()
    list_close = MyQueue()
    list_open.put(problem)
    while True:
        if list_open.empty():
            return False
        current_node = list_open.get()
        print(current_node)
        if current_node == target:
            return True


def action(board):
    board_array = board.get_board()



board1 = Board()
board1 = Board()

q = MyQueue()

q.add_all(board1, board1)
