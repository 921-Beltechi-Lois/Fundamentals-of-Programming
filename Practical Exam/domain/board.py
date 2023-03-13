from texttable import Texttable

from domain.cell import Cell
from exception_validation.exception import ServiceException


class Board:
    def __init__(self):
        self._board = []
        self._rows = 6
        self._columns = 6
        self._first_turn = True  # Order, Computer = True,    Chaos, Player = False


        self._no_of_X = 0
        self._no_of_O = 0

        for i in range(self._rows):
            columns = []
            for j in range(self._columns):
                columns.append(Cell())
            self._board.append(columns)

        self._list_of_row_col =[]

    @property
    def list_of_row_col(self):
        return self._list_of_row_col

    @list_of_row_col.setter
    def list_of_row_col(self, value):
        pass

    @property
    def first_turn(self):
        return self._first_turn

    @first_turn.setter
    def first_turn(self, value):
        self._first_turn = value

    def place_symbol(self, row, col, sym):
        self.validate(row, col, sym)
        self.remember_row_col(row, col)
        if self._first_turn:
            self._board[row][col].selected = True
            self._first_turn = not self._first_turn
            if sym == 'X':
                self._board[row][col].what_sign = 'X'


                self._no_of_X+=1
            if sym == 'O':
                self._board[row][col].what_sign = 'O'


                self._no_of_O+= 1
        else:
            self._board[row][col].selected = True
            self._first_turn = not self._first_turn
            if sym == 'X':
                self._board[row][col].what_sign = 'X'


                self._no_of_X += 1
            if sym == 'O':
                self._board[row][col].what_sign = 'O'

                self._no_of_O += 1
    @property
    def no_of_O(self):
        return self._no_of_O

    @no_of_O.setter
    def no_of_O(self, value):
        pass

    @property
    def no_of_X(self):
        return self._no_of_X

    @no_of_X.setter
    def no_of_X(self, value):
        pass

    def __str__(self):
        t = Texttable()

        for i in range(self._rows):
            lista = []
            for j in range(self._columns):
                cell = self._board[i][j].__str__()
                lista.append(cell)
            t.add_row(lista)

        return t.draw()

    # def hidden_board(self):
    #     t = Texttable()
    #     header = ['', 'A', 'B', 'C', 'D','E','F']
    #     t.add_row(header)
    #
    #     for i in range(self._rows):
    #         lista = [str(i)]
    #         for j in range(self._columns):
    #             cell = self._board[i][j].hidden_board()
    #             lista.append(cell)
    #         t.add_row(lista)
    #
    #     return t.draw()

    def validate(self, row, col, sym):
        if not(row>=0 and row<=5):
            raise ValueError("rows are between 0&5")
        if not (col >= 0 and col <= 5):
            raise ValueError("cols are between 0&5")
        if sym != 'X' and sym !='O':
            raise ValueError("symbol should be X or O")

        if self._board[row][col].selected:
            raise ServiceException("already selected!")

    def remember_row_col(self, row, col):
        self._list_of_row_col.append((row, col))

    def is_board_full(self):
        board_full = True
        for i in range(0,5):
            for j in range(0,5):
                if not(self._board[i][j].selected):
                    board_full=False
        return board_full

    def check_neighbours(self, sym):
        square_1 = 0


        for i in range(0,3):
            for j in range(0,3):
                if self._board[i][j].what_sign == sym:
                    square_1+=1
        square_2 = 0
        for i in range(3, 6):
            for j in range(0, 3):
                if self._board[i][j].what_sign == sym:
                    square_2 += 1

        if square_1> square_2:
            max = square_1
                   #linii   # col
            list = [(0,2), (0,2)]
        else:
            max = square_2
            list = [(0,2), (3,5)]

        square_3 = 0
        for i in range(3, 6):
            for j in range(0, 3):
                if self._board[i][j].what_sign == sym:
                    square_3 += 1
        square_4 = 0
        for i in range(3, 6):
            for j in range(3, 6):
                if self._board[i][j].what_sign == sym:
                    square_4 += 1

        if square_3> square_4:
            max_2 = square_3
            list_2= [(3,5), (0,2)]

        else:
            max_2 =square_4
            list_2 = [(3,5), (3,5)]

        if max > max_2:
            final_list = list
        else:
            final_list = list_2

        return final_list

#
# a = Board()
# print(a)