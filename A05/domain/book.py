class Book:
    def __init__(self, isbn, author, title):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def __str__(self):
        return f'id: {self.__isbn}, author: {self.__author}, title: {self.__title}'


