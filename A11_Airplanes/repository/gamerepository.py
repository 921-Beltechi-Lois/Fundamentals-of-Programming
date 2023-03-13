class GameRepository:
    def __init__(self, game):
        self._game = game

    def get_game_in_progress(self):
        return self._game
