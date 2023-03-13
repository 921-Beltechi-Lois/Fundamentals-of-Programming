class GameService:
    def __init__(self, repository, first_turn, no_of_planes):
        self._repository = repository
        self._first_turn = first_turn
        self._no_of_planes = no_of_planes

    @property
    def no_of_planes(self):
        return self._no_of_planes

    @no_of_planes.setter
    def no_of_planes(self, value):
        self._no_of_planes = value

    @property
    def first_turn(self):
        return self._first_turn

    @first_turn.setter
    def first_turn(self, value):
        self._first_turn = value

    def find_plane(self, x, y):
        """
        First turn :  True ~ Player 1,  False ~ Computer
        Makes a move on the board (depending of who's turn is)
        :param x: given row
        :param y: given column
        :return: 1 ~ Player 1 won  ;   2 ~ Player 2 won ;   0 - no winner so far
        """
        game = self._repository.get_game_in_progress()
        if self._first_turn:
            result = self._make_move(game.board2, x, y)
        else:
            result = self._make_move(game.board1, x, y)
        self._first_turn = not self._first_turn
        return result

    def _make_move(self, board, x, y):
        """
        Makes a move on the opponent board with (x,y) coords
        :param board: given board
        :param x: given row
        :param y: given column
        :return: 1 ~ Player 1 won  ;   2 ~ Player 2 won ;   0 - no winner so far
        """
        board_value = board.find_plane(x, y)
        if board_value == 1:  # cabin found
            board.no_of_planes_left -= 1
        if board.no_of_planes_left == 0:
            if self._first_turn:
                return 1
            else:
                return 2
        return 0

    def lay_plane(self, is_computer, row_cabin, column_cabin, orientation):
        """
        Lays 1 given plane on the board
        :param is_computer: Boolean type True=Computer/False=Player1
        :param row_cabin: given x
        :param column_cabin: given y
        :param orientation: North, West, East, South
        :return: successfully created, otherwise it will raise exceptions
        """
        game = self._repository.get_game_in_progress()
        if is_computer:
            game.board2.lay_planes(row_cabin, column_cabin, orientation)
        else:
            game.board1.lay_planes(row_cabin, column_cabin, orientation)

    def computer_attempt_to_win(self):
        """
        Computer will block player1 to win if there is a possible 1-move victory apart
        :return: the coords of the last cabin (of the player1's board), if this situation not occurred --> false

        If Player found the (total_no_of_planes - 1) and the computer has found also (total_no_of_planes - 1) \
        and it is his turn (computer's), then he will find the cabin place by going into his player 1's board (strategy
        is more like a cheat code because he has to block whenever possible in this case)
        """
        game = self.get_game_in_progress()
        board_1_no_of_planes_left = game.board1.no_of_planes_left  # computer guessing    # another getter for planes nr
        board_2_no_of_planes_left = game.board2.no_of_planes_left  # player 1 guessing
        if board_1_no_of_planes_left == 1 and board_2_no_of_planes_left == 1 \
                and not self._first_turn:  # 2-2 on planes and it is computer's turn
            row = game.board1.rows
            column = game.board1.columns
            board_1 = game.board1.board
            for i in range(row):
                for j in range(column):
                    if board_1[i][j].cabin and not board_1[i][j].is_selected:
                        result = self.find_plane(i, j)
                        return result  # computer wins whenever possible, return 2
        return 0

    def get_game_in_progress(self):
        return self._repository.get_game_in_progress()
