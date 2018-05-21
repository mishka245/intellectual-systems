"""
created by Mikheil Lomidze
Just for educational purposes
AI tic tac toe
Implemented with Minmax algorithm

"""
import os
import sys

# To run from main dir
sys.path.append(os.getcwd())
from enum import Enum

VIEW_TEMPLATE = """-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
------------- """


class Player(Enum):
    """
    Player 1 -> X
    Player 2 -> 0
    """
    NONE = 0
    PLAYER1 = 1
    PLAYER2 = 2


class IllegalAreaIndexesException(Exception):
    pass


class AreaAlreadyChoosenException(Exception):
    pass


class Board:
    WINNING_LINES = (
        # Horizontal cases
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # Vertical cases
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # Cross cases
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    def __init__(self, board=None):
        if board:
            self.array = board.get_array()
        else:
            self.array = []
            for i in range(3):
                self.array.append([Player.NONE, Player.NONE, Player.NONE])

    def __str__(self):
        chars = []
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == Player.PLAYER1:
                    chars.append('X')
                elif self.array[i][j] == Player.PLAYER2:
                    chars.append('O')
                else:
                    chars.append(" ")
        return VIEW_TEMPLATE.format(*chars)

    def choose_area(self, x: int, y: int, player: Player):
        if player.value not in (1, 2):
            raise Exception("Illegal player!")
        if x not in range(3) or y not in range(3):
            raise IllegalAreaIndexesException("Area indexes are not in range!")
        if self.array[x][y] != Player.NONE:
            raise AreaAlreadyChoosenException
        self.array[x][y] = player

    def reset_area(self, x: int, y: int):
        self.array[x][y] = Player.NONE

    def get_winner(self) -> Player:
        for line in self.WINNING_LINES:
            if self.array[line[0][0]][line[0][1]] == self.array[line[1][0]][line[1][1]] == self.array[line[2][0]][
                line[2][1]]:
                if self.array[line[0][0]][line[0][1]].value in (1, 2):
                    return self.array[line[0][0]][line[0][1]]
        if self.get_free_areas() == 0:
            return Player.NONE
        else:
            return None

    def get_array(self):
        return self.array

    def get_free_areas(self) -> int:
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.array[i][j].value == Player.NONE.value:
                    counter += 1
        return counter

    def left_movement(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == Player.NONE:
                    return True
        return False


class AIMove:
    def __init__(self, x: int, y: int, player: Player):
        self.x = x
        self.y = y
        self.player = player
        self.score = None

    def __str__(self):
        return " ".join([str(self.x), str(self.y), "player -", str(self.player.value)])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def set_score(self, value):
        self.score = value

    def get_score(self):
        return self.score


def get_ai_move(board: Board, player: Player) -> AIMove:
    winner = board.get_winner()
    if winner:
        move = AIMove(None, None, None)
        if winner.value == Player.PLAYER1.value:
            move.set_score(10)
            return move
        elif winner.value == Player.PLAYER2.value:
            move.set_score(-10)
            return move
        elif winner.value == Player.NONE.value:
            move.set_score(0)
            return move

    moves = []

    for i in range(3):
        for j in range(3):
            if board.get_array()[i][j] == Player.NONE:
                ai_move = AIMove(i, j, player)
                board.choose_area(i, j, player)
                if player.value == Player.PLAYER1.value:
                    ai_move.set_score(get_ai_move(board, Player.PLAYER2).get_score())
                else:
                    ai_move.set_score(get_ai_move(board, Player.PLAYER1).get_score())
                moves.append(ai_move)
                board.reset_area(i, j)

    best_move = None

    if player.value == Player.PLAYER1.value:
        best_score = -2000000000
        for m in moves:
            if m.get_score() > best_score:
                best_score = m.get_score()
                best_move = m
    else:
        best_score = 2000000000
        for m in moves:
            if m.get_score() < best_score:
                best_score = m.get_score()
                best_move = m

    return best_move


def someone_won(board):
    print(board)
    winner = board.get_winner()
    if winner:
        if winner.value == Player.PLAYER1.value:
            print("AI WINS!")
        elif winner.value == Player.PLAYER2.value:
            print("Player wins!")
        else:
            print("Draw!")
        return True
    return False


board = Board()

# hardcoded AI turn to decrease quantity of possibilities
board.choose_area(1, 1, Player.PLAYER1)
print("CPU choose", 1, 1)
print(board)

# user turn
player_choice = input("Choose area -  ")
player_coords = []
for i in map(int, player_choice.split()):
    player_coords.append(i)
board.choose_area(player_coords[0], player_coords[1], Player.PLAYER2)
print(board)
print("-" * 80)

print("Welcome to Tic Tac Toe game!!!")
while True:
    # AI turn
    cpu_choice = get_ai_move(board, Player.PLAYER1)
    print("CPU choose - ", cpu_choice)
    board.choose_area(cpu_choice.getX(), cpu_choice.getY(), Player.PLAYER1)
    if someone_won(board):
        break
    # user turn
    player_choice = input("Choose area -  ")
    player_coords = []
    for i in map(int, player_choice.split()):
        player_coords.append(i)
    board.choose_area(player_coords[0], player_coords[1], Player.PLAYER2)
    if someone_won(board):
        break
    print("-" * 80)
