"""
Rules

-draw both valid planes (x3 each)
- random start from player 1 vs computer
- player 1 tries to guess, player 2 can do:
	1. air = no match on a plane
	2. touched / lovit = a piece of plane, but not the cabin!
	3. down / mort /doborat = cabin of a plane hited, all other 'pieces' of the plane will be 'destroyed'
	signs: X = lovit, ' ' = aer
	 X = hited, CABINA = '$',   0 = air, nothing, non-visible = *

'Un jucător nu este neapărat nevoit să spună în ce direcție se află avionul doborât de către adversar.
 Astfel, jucătorul nu este nevoit să spună dacă o căsuță lovită face parte dintr-un avion deja doborât.'

How do you win?: first player that finds those 3 cabins.

Draw: First player that had the advantage of start found 3 cabines, second player has another chance of finding the plane

"""
import random


class UI:
    def __init__(self, service):
        self._service = service
        self._no_of_planes = self._service.no_of_planes
        self._first_turn = self._service.first_turn

        game = self._service.get_game_in_progress()
        self._rows = game.board1.rows
        self._columns = game.board1.columns

    def lay_plane_ui(self):
        print('Input the cabin position (x, y)')
        position_x = int(input('cabin position row: '))
        position_y = int(input('cabin position column: '))
        print('orientation (N,S,E,W): ')
        orientation = input()
        self._service.lay_plane(False, position_x, position_y, orientation)

    def lay_random_plane_for_computer_ui(self):
        row_cabin = random.randint(0, self._rows - 1)
        column_cabin = random.randint(0, self._columns - 1)
        possibilities = ['N', 'S', 'W', 'E']
        orientation = random.choice(possibilities)
        self._service.lay_plane(True, row_cabin, column_cabin, orientation)

    def show_game(self):
        game = self._service.get_game_in_progress()
        print("Player 1's BOARD: ")
        print(game.board1)
        print()
        print("Computer's BOARD: ")
        print(game.board2.hidden_board())

    """"
    Player 1 vs Computer (we can set computer's moves)
    def find_planes_ui(self):
        print("Destroy plane: Type in the row and column of your opponent! ")
        if self._service.first_turn:
            print('Player 1 turn')
        else:
            print('Computer turn')
        row = int(input('row: '))
        column = int(input('column: '))
        winner_id = self._service.find_plane(row, column)
        return winner_id
    """

    def find_planes_ui(self):
        if self._service.first_turn:
            print("Destroy plane: Type in the row and column of your opponent! ")
            game = self._service.get_game_in_progress()
            board_2 = game.board2.board
            board_2_planes = game.board2.no_of_planes_left
            print("You've got " + str(board_2_planes) + " planes left to guess")
            coords = False
            while not coords:
                print('Player 1 turn')
                row = int(input('row: '))
                column = int(input('column: '))
                if board_2[row][column].is_selected:
                    print("You already attacked there, choose other coords")
                else:
                    coords = True
            print()
            print('Player 1 attacked at: ', row, column)
            print()
        else:
            game = self._service.get_game_in_progress()
            board_1 = game.board1.board
            board_1_planes = game.board1
            coords = False
            print('Computer turn')
            print("Computer has " + str(board_1_planes.no_of_planes_left) + " planes left to guess")
            while not coords:
                row = random.randint(0, self._rows - 1)
                column = random.randint(0, self._columns - 1)
                if board_1[row][column].is_selected:
                    pass
                else:
                    coords = True
            print()
            print('Computer attacked at: ', row, column)
            print()

        winner_id = self._service.find_plane(row, column)
        return winner_id

    def start(self):
        no_of_planes_left = self._no_of_planes
        print("Player 1 will choose plane's places!\n")
        while True:
            self.show_game()
            try:  # Placing Planes - Player 1
                self.lay_plane_ui()
                no_of_planes_left -= 1
                print("you've got " + no_of_planes_left + " planes left to place!")
            except Exception as e:
                print(str(e))
            if no_of_planes_left == 0:
                break

        no_of_planes_left = self._no_of_planes
        while True:
            try:  # Placing Planes - Computer
                self.lay_random_plane_for_computer_ui()
                no_of_planes_left -= 1
            except Exception:
                pass
            if no_of_planes_left == 0:
                break

        print("Computer has chosen the plane places")
        self.show_game()
        no_of_planes_left = self._no_of_planes

        # cmd = input()
        # if cmd == '22':
        #     game = self._service.get_game_in_progress()
        #     print('cheat code activated')
        #     print(game.board2)
        #     print()

        while True:  # Finding Planes
            try:
                # cmd = input()
                # if cmd == '22':
                #     game = self._service.get_game_in_progress()
                #     print('cheat code activated >> Computer board revealed')
                #     print(game.board2)
                #     print()

                winner_id = self.find_planes_ui()
                computer_wins = self._service.computer_attempt_to_win()
                if computer_wins == 2:  # 2 if computer wins
                    winner_id = 2
                if winner_id == 1:
                    game = self._service.get_game_in_progress()
                    board_2 = game.board2
                    if self._first_turn and board_2.no_of_planes_left == no_of_planes_left - 1:  # possible DRAW, computer will have 1 more round
                        winner_id = self.find_planes_ui()
                        if winner_id == 2:
                            self.show_game()
                            print("DRAW!")
                            return
                    self.show_game()
                    print("Player 1 won!")
                    return
                elif winner_id == 2:
                    game = self._service.get_game_in_progress()
                    board_1 = game.board1
                    if not self._first_turn and board_1.no_of_planes_left == no_of_planes_left - 1:  # possible DRAW, player1 will have 1 more round
                        winner_id = self.find_planes_ui()
                        if winner_id == 1:
                            self.show_game()
                            print("DRAW!")
                            return
                    self.show_game()
                    print("Player 2 won!")
                    return

                self.show_game()
                print("\n\n\n")
                print("-----------------------------------------------------------------------")
            except Exception as e:
                print(e)