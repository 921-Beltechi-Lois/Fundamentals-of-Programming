from copy import deepcopy

from Tools.scripts.find_recursionlimit import test_add

from src.domain.book import Book


class BookService:
    def __init__(self):
        self._book_list = []
        self._undo_list = []

    # def create_book(self, isbn, author, title):
    # book = Book(isbn, author, title)
    # if not (isbn.isnumeric()):
    # raise ValueError("given data input is wrong, all parameters must be strings")
    # self._book_list[isbn] = book

    def __check_duplicity(self, isbn, title):
        """
        Checks if isbn is unique, or the given title
        :param isbn: id
        :param title: title
        :return: returns true if there is no duplicity found, otherwise a message
        """
        for book in self._book_list:
            if book.isbn == isbn:
                raise ValueError("duplicate isbn given")
            if book.title == title:
                raise ValueError("duplicate title given")
        return 1

    def __create_book(self, isbn, author, title):
        """

        :param isbn: Numerical string isbn
        :param author: string author
        :param title: string title
        :return: Creates in class book a new book, otherwise it returns 0
        """
        try:
            if not (isbn.isnumeric() == 1 and author.isnumeric() == 0 and title.isnumeric() == 0):
                raise ValueError("wrong data introduced")
            return Book(isbn, author, title)
        except ValueError as ve:
            print(str(ve))

    def add_book(self, isbn, author, title):
        """
        Adds a book to the list
        :param isbn: id of book
        :param author: author
        :param title: title
        :return: Appends the elements of a book to the list, otherwise a message will by shown in case of duplicity
        """

        if self.__check_duplicity(isbn, title):
            self._undo_list.append(self._book_list[:])
            self._book_list.append(self.__create_book(isbn, author, title))

    def generate_books(self):
        self._book_list = [
            self.__create_book('123', 'John Steinbeck', 'East of Eden'),
            self.__create_book('124', 'F. Scott Fitzgerald', 'The Great Gatsby'),
            self.__create_book('125', 'George Orwell', 'jnjn4'),
            self.__create_book('220', 'George Orwell', 'Animal Farm'),
            self.__create_book('235', 'Ernest Hemingway', 'A Farewell to Arms'),
            self.__create_book('653', 'John Fowles', 'The Collector'),
            self.__create_book('657', 'Virginia Woolf', 'To the Lighthouse'),
            self.__create_book('900', ' Giovanni Boccaccio', 'The Decameron'),
            self.__create_book('543', 'Ben Rice', 'Pobby and Dingan'),
            self.__create_book('12', 'John Boyne', 'The Boy in the Striped Pajamas')
        ]
        self._undo_list.append(self._book_list[:])
        # for i in range(1, 11):
        #     book = self.__create_book('isbn' + str(i), 'author' + str(i), 'title' + str(i))
        #     self._book_list.append(book)

    def filter_list_by_removing_books_with_a_given_title(self, title_word):
        filtered_list = []
        initial_list = deepcopy(self._book_list)
        self._undo_list.append(self._book_list[:])
        for book in self._book_list:
            if not (book.title.startswith(title_word)):  # if it does not start with the given word
                filtered_list.append(book)
        self._book_list[:] = filtered_list
        if len(initial_list) == len(self._book_list):
            self._undo_list.remove(len(self._undo_list) - 1)
            raise ValueError("no such title starts with the given word")
        return self._book_list

    def undo(self):
        """
        undo
        :return: un-did
        """
        if len(self._undo_list) >= 2:
            self._book_list[:] = self._undo_list[len(self._undo_list) - 1]  # equal to initial list
            del self._undo_list[len(self._undo_list) - 1]  # deletes last one in the list
        else:
            print('Nothing left to Undo')
            #self._book_list[:] = self._undo_list[0]

    def get_all(self):
        return self._book_list
        # return deepcopy(list(self._book_list.values()))


def test_add():

    #testing add_book



    isbn = "100"
    author = 'Name'
    title = 'abc'
    b = BookService()
    b.add_book(isbn, author, title)
    list = b.get_all()
    assert len(list) == 1
    assert list[0].isbn == isbn
    assert list[0].author == author
    assert list[0].title == title

    try:
        isbn = "ytr"
        author = "idk"
        title = "uiy"
        b.add_book(isbn, author, title)
    except ValueError as ve:
        assert True


test_add()


"""
test
"""
