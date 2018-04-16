from lib.board import Board
from lib.my_queue import MyQueue

MOVES = [(0, -1), (-1, 0), (0, 1), (1, 0)]
TARGET_STATE = Board([1, 2, 3, 4, 5, 6, 7, 8, 0])


def insert_all(child_nodes, list_open, list_close):
    for node in child_nodes:
        if node not in list_open and node not in list_close:
            list_open.put(node)


def verify_coords(new_coords):
    if new_coords[0] < 0 or new_coords[0] > 2:
        return False
    if new_coords[1] < 0 or new_coords[1] > 2:
        return False
    return True


def action(board):
    parent_array = board.get_board_as_list()
    parent_coords = board.get_coords()
    result = []
    for move in MOVES:
        new_coords = (parent_coords[0] + move[0], parent_coords[1] + move[1])
        if verify_coords(new_coords):
            b = Board(parent_array)
            b.swap(parent_coords, new_coords)
            result.append(b)
    return result


def tree_search(problem, target):
    iteration_number = 0
    list_open = MyQueue()
    list_close = MyQueue()
    list_open.put(problem)
    while True:
        if list_open.empty():
            return False
        current_node = list_open.get()
        print("Iteration: {i}; Open: {o}; Closed: {c}"
              .format(i=iteration_number, o=list_open.qsize(), c=list_close.qsize()))
        print(current_node)
        if current_node == target:
            return True
        child_nodes = action(current_node)
        insert_all(child_nodes, list_open, list_close)
        iteration_number += 1
        list_close.put(current_node)


test_board = Board([1, 2, 3, 4, 5, 6, 0, 7, 8])
test_board_1 = Board()

print(tree_search(test_board_1, TARGET_STATE))
