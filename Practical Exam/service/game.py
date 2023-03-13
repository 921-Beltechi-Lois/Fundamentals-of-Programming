class Game:
    def __init__(self, board):
        self._game = board

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value