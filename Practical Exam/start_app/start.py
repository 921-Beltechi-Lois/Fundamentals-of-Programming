from domain.board import Board
from service.game import Game
from ui.ui import UI

board = Board()
game = Game(board)
ui = UI(board, game)
ui.start()