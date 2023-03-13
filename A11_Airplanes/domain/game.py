from domain.board import Board


class Game:
    def __init__(self, columns, rows):
        self._id = 1
        self._board1 = Board(columns, rows)
        self._board2 = Board(columns, rows)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def board1(self):
        return self._board1

    @board1.setter
    def board1(self, value):
        self._board1 = value

    @property
    def board2(self):
        return self._board2

    @board2.setter
    def board2(self, value):
        self._board2 = value
