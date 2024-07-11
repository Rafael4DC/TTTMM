from enum import Enum


class Symbol(Enum):
    X = "X"
    O = "O"


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]]
        self.players = [player1, player2]
        self.turn = Symbol.X

    def swap_turn(self):
        if self.turn == Symbol.X:
            self.turn = Symbol.O
        else:
            self.turn = Symbol.X

    def get_current_player(self):
        if self.players[0].symbol == self.turn:
            return self.players[0].name
        else:
            return self.players[1].name

    def make_move(self, y, x):
        if self.board[x][y] is None:
            self.board[x][y] = self.turn
            self.swap_turn()
            return True
        return False

    def victory_condi(self):
        winner = None

        #Horizontal 3
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][
            0] is not None:
            winner = self.board[0][0]
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][
            0] is not None:
            winner = self.board[1][0]
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][
            0] is not None:
            winner = self.board[2][0]

        #Vertical 3
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[2][
            0] is not None:
            winner = self.board[2][0]
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[2][
            1] is not None:
            winner = self.board[2][1]
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[2][
            2] is not None:
            winner = self.board[2][2]

        #Diagonal 2
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][
            0] is not None:
            winner = self.board[1][1]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][
            1] is not None:
            winner = self.board[1][1]

        return winner
