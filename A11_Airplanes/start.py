import random

from domain.game import Game
from repository.gamerepository import GameRepository
from service.gameservice import GameService

from ui.ui import UI



no_of_planes = 3
players = [True, False]  # True = Player 1, False = Computer
first_turn = random.choice(players)
print(first_turn)

game = Game(10, 10)
repository = GameRepository(game)
service = GameService(repository, first_turn, no_of_planes)
ui = UI(service)
ui.start()




