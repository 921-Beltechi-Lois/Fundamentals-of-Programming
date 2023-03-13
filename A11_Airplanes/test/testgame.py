import unittest

from domain.game import Game
from exception.validation_exception import ValidationException
from repository.gamerepository import GameRepository
from service.gameservice import GameService


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        """
        Runs before every test method
        """
        first_turn = True  # first player starts
        no_of_planes = 3
        game = Game(10, 10)
        repository = GameRepository(game)
        service = GameService(repository, first_turn, no_of_planes)

        self._service = service

        self._board1 = game.board1.board
        self._board2 = game.board2.board

        # self.test_add_fail()
        # self.test_add_success()

    def test_lay_plane(self):
        row_cabin1_player1 = 5
        column_cabin1_player1 = 5
        orientation = 'W'

        self._service.lay_plane(False, row_cabin1_player1, column_cabin1_player1, orientation)

        board_1 = self._service.get_game_in_progress().board1.board  # todo??
        self.assertEqual(board_1[row_cabin1_player1][column_cabin1_player1].cabin, True)  # cabin tested
        self.assertEqual(board_1[row_cabin1_player1 - 2][column_cabin1_player1 + 1].part_of_plane,
                         True)  # all parts of plane tested
        self.assertEqual(board_1[row_cabin1_player1 - 1][column_cabin1_player1 + 1].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1][column_cabin1_player1 + 1].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1 + 1][column_cabin1_player1 + 1].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1 + 2][column_cabin1_player1 + 1].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1][column_cabin1_player1 + 2].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1 + 1][column_cabin1_player1 + 3].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1][column_cabin1_player1 + 3].part_of_plane, True)
        self.assertEqual(board_1[row_cabin1_player1 - 1][column_cabin1_player1 + 3].part_of_plane, True)

        self.assertEqual(board_1 not in self._board1, True)  # board1 changed

        row_cabin2_player1 = 11
        column_cabin2_player1 = 12
        orientation = 'N'
        with self.assertRaises(ValidationException) as re:
            self._service.lay_plane(False, row_cabin2_player1, column_cabin2_player1,
                                    orientation)  # todo add plane failed
        self.assertEqual('Plane placed out of the board game', str(re.exception))

        row_cabin3_player1 = 5
        column_cabin3_player1 = 5
        orientation = 'S'
        with self.assertRaises(ValidationException) as re:
            self._service.lay_plane(False, row_cabin3_player1, column_cabin3_player1,
                                    orientation)  # todo add plane failed
        self.assertEqual('Plane collision detected at position (' + '5' + ', ' + '5' + ')', str(re.exception))

    def test_find_plane(self):
        # game 1
        row_cabin1_player1 = 5
        column_cabin1_player1 = 5
        orientation = 'W'
        self._service.lay_plane(False, row_cabin1_player1, column_cabin1_player1, orientation)  # player 1

        row_cabin1_player2 = 6
        column_cabin1_player2 = 2
        orientation = 'N'
        self._service.lay_plane(True, row_cabin1_player1, column_cabin1_player1, orientation)  # computer 1 ~ player 2

        # Player 1 will find player 2's planes
        result = self._service.find_plane(0, 0)
        self.assertEqual(result, 0)  # todo no part of plane / cabin destroyed
        board_2 = self._service.get_game_in_progress().board2
        self.assertEqual(board_2.no_of_planes_left, 1)  # todo    nothing found
        board_22 = self._service.get_game_in_progress().board2.board
        self.assertEqual(board_22[0][0].is_selected, True)
        self.assertEqual(board_22[0][0].cabin, False)
        self.assertEqual(board_22[0][0].part_of_plane, False)

        # Player 2 will find player 1's planes
        result = self._service.find_plane(row_cabin1_player1, column_cabin1_player1)
        self.assertEqual(result, 2)  # one destoyed cabin - and we already have a winner ~ player 2
        board_1 = self._service.get_game_in_progress().board1
        self.assertEqual(board_1.no_of_planes_left, 0)  # todo found a cabin - no.of.planes = 0 -> winner

        board_11 = self._service.get_game_in_progress().board1.board
        self.assertEqual(board_11[row_cabin1_player1][column_cabin1_player1].is_selected, True)  # cabin was selected

    def test_computer_attempt_to_win(self):
        """
        Minimally, the computer player should move to win the game whenever possible and should block the human \
        player’s attempts at 1-move victory, whenever possible

        If Player found the (total_no_of_planes - 1) and the computer has found also (total_no_of_planes - 1) \
        and it is his turn (computer's), then he will find the cabin place by going into his player 1's board (strategy
        is more like a cheat code because he has to block whenever possible in this case)

        Possible case of winning:
        3 planes()
            Player 1 starts:
            -player found first cabin of the computer
            -computer found first cabin of the player
            -player found second cabin of the computer
            -computer found the second cabin of the player
            -player does not find a cabin (here it is a possibility for computer to win);
              (if player would've found the third cabin :  --> Player 1 was first  + Player wins for now, \
                but COMPUTER still has a chance for DRAW)
            -computer found the third one and blocked the player

        """
        row_cabin1_player1 = 5
        column_cabin1_player1 = 5
        orientation = 'W'
        self._service.lay_plane(False, row_cabin1_player1, column_cabin1_player1, orientation)  # player 1  #1

        row_cabin2_player1 = 0
        column_cabin2_player1 = 2
        orientation = 'N'
        self._service.lay_plane(False, row_cabin2_player1, column_cabin2_player1, orientation)  # player 1  #2

        row_cabin3_player1 = 6
        column_cabin3_player1 = 2
        orientation = 'N'
        self._service.lay_plane(False, row_cabin3_player1, column_cabin3_player1, orientation)  # player 1  #3

        row_cabin1_player2 = 0
        column_cabin1_player2 = 7
        orientation = 'N'
        self._service.lay_plane(True, row_cabin1_player2, column_cabin1_player2, orientation)  # computer 1 ~ player 2

        row_cabin2_player2 = 6
        column_cabin2_player2 = 2
        orientation = 'N'
        self._service.lay_plane(True, row_cabin2_player2, column_cabin2_player2, orientation)  # computer 1 ~ player 2

        row_cabin3_player2 = 0
        column_cabin3_player2 = 2
        orientation = 'N'
        self._service.lay_plane(True, row_cabin3_player2, column_cabin3_player2, orientation)  # computer 1 ~ player 2

        self._service.find_plane(row_cabin1_player2, column_cabin1_player2)  # player1 starts and finds the # 1cabin
        self._service.find_plane(row_cabin1_player1, column_cabin1_player1)  # computer finds the #1 cabin
        self._service.find_plane(row_cabin2_player2, column_cabin2_player2)  # player1 finds the #2 cabin
        self._service.find_plane(row_cabin2_player1, column_cabin2_player1)  # computer finds the #2 cabin
        self._service.find_plane(0, 0)  # Player 1 gives wrong coords for the computer's planes
        result = self._service.computer_attempt_to_win()  # computer will use this function in order to block the player
        self.assertEqual(result, 2)  # computer wins, winner_id = 2

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass
