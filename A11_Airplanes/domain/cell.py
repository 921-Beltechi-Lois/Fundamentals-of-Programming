class Cell:
    def __init__(self):
        self._selected = False
        self._cabin = False
        self._part_of_plane = False

    @property
    def is_selected(self):
        return self._selected

    @is_selected.setter
    def is_selected(self, value):
        self._selected = value

    @property
    def cabin(self):
        return self._cabin

    @cabin.setter
    def cabin(self, value):
        self._cabin = value

    @property
    def part_of_plane(self):
        return self._part_of_plane

    @part_of_plane.setter
    def part_of_plane(self, value):
        self._part_of_plane = value

    def __str__(self):
        """
        Player1's cell (guessed by the computer)
        :return: characters
        """
        if self._selected:   # computer's selected smth
            if self._cabin:
                return '&'
            if self._part_of_plane:
                return '%'
            return 'X'

        if self._cabin:         # player 1's initial board
            return '@'
        if self._part_of_plane:
            return '#'
        return ' '

    def hidden_cell(self):
        """
        Computer's cell (guessed by the player1)
        :return: char: different signs
        """
        if self._selected:
            if self._cabin:
                return '@'
            if self._part_of_plane:
                return '#'
            return 'X'
        return ' '
