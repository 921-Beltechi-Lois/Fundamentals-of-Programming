class Cell:
    def __init__ (self):
        self._selected = False
        self._what_sign = ''

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    @property
    def what_sign(self):
        return self._what_sign

    @what_sign.setter
    def what_sign(self, value):
        self._what_sign = value

    def __str__(self):
        if self._selected:
            if self._what_sign == 'X':
                return 'X'
            return 'O'
        return ' '
