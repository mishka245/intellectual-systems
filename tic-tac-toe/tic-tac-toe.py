"""
created by Mikheil Lomidze
Just for educational purposes
AI tic tac toe

"""
import sys
import os

# To run from main dir
sys.path.append(os.getcwd())
from enum import Enum


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

    def __init__(self):
        self.array = []
        for i in range(3):
            self.array.append([Player.NONE, Player.NONE, Player.NONE])

    def choose_area(self, x: int, y: int, player: Player):
        if player.value not in (1, 2):
            raise Exception("Illegal player!")
        if x not in range(3) or y not in range(3):
            raise IllegalAreaIndexesException("Area indexes are not in range!")
        if self.array[x][y] != Player.NONE:
            raise AreaAlreadyChoosenException
        self.array[x][y] = player

    def get_winner(self)-> Player:
        for line in self.WINNING_LINES:
            if self.array[line[0][0]][line[0][1]] == self.array[line[1][0]][line[1][1]] == self.array[line[2][0]][line[2][1]]:
                if self.array[line[0][0]][line[0][1]].vaalue in (1, 2):
                    return self.array[line[0][0]][line[0][1]]
        return Player.NONE

