from src.exception.service_exception import ServiceException


class UndoRedoService:
    """
        How can we implement multiple undo/redo with cascade?

        1. Keep track of program operations and reverse them (undo) / repeat them (redo)
            => Command design pattern
            (command = tell the program to do something, but later)

        2. Keep copies of repositories at each operation (deep-copy)
            => Memento design pattern (remember the state of the repos and restore them)
            (kinda like A34)

        3. State-diffing
            1. + 2.
        """

    def __init__(self):
        self._history = []
        self._index = -1

    def __check_index_position(self):
        if self._index != len(self._history) - 1:
            if self._index == -1:
                self._history = []
                self._index = -1
            else:
                self._history = self._history[:self._index]

    def record(self, operation):
        self.__check_index_position()
        self._history.append(operation)
        self._index = len(self._history) - 1  # last op   [-1] initial

    def undo(self):
        if self._index == -1:
            raise ServiceException("No more undos")
        # self._index -= 1
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index == len(self._history) - 1:  # last item in the history list
            raise ServiceException("No more redos")
        self._index += 1
        self._history[self._index].redo()


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)





class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()
