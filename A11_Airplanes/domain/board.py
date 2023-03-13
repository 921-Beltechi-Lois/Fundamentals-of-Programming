from texttable import Texttable

from domain.cell import Cell
from exception.validation_exception import ValidationException


class Board:
    def __init__(self, columns, rows):
        self._columns = columns
        self._rows = rows
        self._no_of_planes_left = 0
        self._board = [[Cell() for _ in range(self._columns)] for _ in range(self._rows)]
        # todo self.lay_planes(self._no_of_planes) out

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value

    @property
    def no_of_planes_left(self):
        return self._no_of_planes_left

    @no_of_planes_left.setter
    def no_of_planes_left(self, value):
        self._no_of_planes_left = value

    def find_plane(self, row, column):
        """
        Board is marked with 2 posibilities: @ = cabin, # = part of plane, also the cell is selected
        :param row: given x
        :param column: given y
        :return: 1 ~ if cabin is found ;  2 ~ if a part of the plane is found ;  0 ~ nothing found
        """
        # 1 = cabin, 2 = part of plane, 0 nothing
        self._board[row][column].is_selected = True
        if self._board[row][column].cabin:
            return 1
        elif self._board[row][column].part_of_plane:
            return 2
        return 0

    def lay_planes(self, row_cabin, column_cabin, orientation):
        """
        Lay a valid plane on the board with the given orientation, row_cabin & column_cabin, showing its selection on the \
        board and the number of planes added are increased (used in service to see if the total number of planes has been \
        added)

        :param row_cabin: given x
        :param column_cabin: given y
        :param orientation: given orientation 'N', 'S', 'W', 'E'
        :return: if not successfully added it will raise an exception
        """
        self.validate_cell(row_cabin, column_cabin)

        if orientation == 'N':
            positions = self.create_north(row_cabin, column_cabin)
        elif orientation == 'S':
            positions = self.create_south(row_cabin, column_cabin)
        elif orientation == 'E':
            positions = self.create_east(row_cabin, column_cabin)
        elif orientation == 'W':
            positions = self.create_west(row_cabin, column_cabin)
        else:
            raise ValidationException('Invalid orientation')

        self._board[row_cabin][column_cabin].cabin = True
        for position in positions:
            self._board[position[0]][position[1]].part_of_plane = True
        self._no_of_planes_left += 1

    def create_north(self, row_cabin, column_cabin):
        """
        Used when creating a plane placed with the cabin in the north side
        :param row_cabin: given x
        :param column_cabin: given y
        :return: a list of planes positions (without the cabin)
        """

        c = [2, 0, 1]
        index = 0
        positions = []
        for i in range(row_cabin + 1, row_cabin + 4):
            for j in range(column_cabin - c[index], column_cabin + c[index] + 1):
                self.validate_cell(i, j)
                positions.append((i, j))
            index += 1
        return positions

    def create_south(self, row_cabin, column_cabin):

        """
        Used when creating a plane placed with the cabin in the south side
        :param row_cabin: given x
        :param column_cabin: given y
        :return: a list of planes positions (without the cabin)
        """
        c = [2, 0, 1]
        index = 0
        positions = []
        for i in range(row_cabin - 1, row_cabin - 4, -1):
            for j in range(column_cabin - c[index], column_cabin + c[index] + 1):
                self.validate_cell(i, j)
                positions.append((i, j))
            index += 1
        return positions

    def create_west(self, row_cabin, column_cabin):
        """
        Used when creating a plane placed with the cabin in the west side
        :param row_cabin: given x
        :param column_cabin: given y
        :return: a list of planes positions (without the cabin)
        """
        c = [2, 0, 1]
        index = 0
        positions = []
        for j in range(column_cabin + 1, column_cabin + 4):
            for i in range(row_cabin - c[index], row_cabin + c[index] + 1):
                self.validate_cell(i, j)
                positions.append((i, j))
            index += 1
        return positions

    def create_east(self, row_cabin, column_cabin):
        """
        Used when creating a plane placed with the cabin in the east side
        :param row_cabin: given x
        :param column_cabin: given y
        :return: a list of planes positions (without the cabin)
        """
        c = [2, 0, 1]
        index = 0
        positions = []
        for j in range(column_cabin - 1, column_cabin - 4, -1):
            for i in range(row_cabin - c[index], row_cabin + c[index] + 1):
                self.validate_cell(i, j)
                positions.append((i, j))
            index += 1
        return positions

    def validate_cell(self, i, j):
        """
        Validate the cell coords (x,y)
        :param i: given x
        :param j: given y
        :return: raises exception if the coords are out of the board // there is already placed a plane there
        """
        if not (0 <= i < self._rows and 0 <= j < self._columns):
            raise ValidationException('Plane placed out of the board game')
        if self._board[i][j].part_of_plane or self._board[i][j].cabin:
            raise ValidationException('Plane collision detected at position (' + str(i) + ', ' + str(j) + ')')

    def __str__(self):
        """
        player's board
        :return: table
        """
        t = Texttable()

        header = list(range(self._columns))
        t.header(['/', ""] + header)

        # for row in range(self._rows):
        #     str_row = [self._board[row][i].__str__() for i in range(self._columns)]
        #     t.add_row([str(row), "|"] + str_row)
        #
        for row in range(self._rows):
            t.add_row([str(row), "|"] + self._board[row])
        return t.draw()

    def hidden_board(self):
        """
        printing computer's board
        :return: a table
        """
        t = Texttable()

        header = list(range(self._columns))
        t.header(['/', ""] + header)

        for row in range(self._rows):
            str_row = [self._board[row][i].hidden_cell() for i in range(self._columns)]
            t.add_row([str(row), "|"] + str_row)
        return t.draw()
