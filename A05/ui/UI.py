from src.domain.book import Book
from src.services.book_service import BookService


class BooksUI:
    def __init__(self, service):
        self.__book_service = service

    def _print_menu(self):
        print("Option 1: Add a book")
        print("Option 2: Display the list of books")
        print("Option 3: Filter the list so that book titles starting with a given word are deleted from the list")
        print("Option 4: Undo the last operation that modified program data.")
        print("Option 5: Exit")

    def _show_book_list_ui(self):
        for book in self.__book_service.get_all():
            print(book)

    def _create_book_ui(self):
        try:
            isbn = input("isbn: ")
            author = input("author: ")
            title = input("title: ")
            if isbn.isnumeric():
                self.__book_service.add_book(isbn, author, title)
            else:
                raise ValueError("isbn must be a number")
        except ValueError as ve:
            print(str(ve))

    def _filter_list_by_removing_books_with_a_given_title_ui(self):
        try:
            title_word = input("Book titles starting with a given word are deleted from the list, title name: ")
            title_word = title_word.title()
            self.__book_service.filter_list_by_removing_books_with_a_given_title(title_word)
        except ValueError as ve:
            print(ve)

    def _undo_ui(self):
        self.__book_service.undo()

    def start(self):
        while True:
            self._print_menu()
            option = input("Choose your option: ")
            if option == '1':
                self._create_book_ui()
            elif option == '2':
                self._show_book_list_ui()
            elif option == '3':
                self._filter_list_by_removing_books_with_a_given_title_ui()
            elif option == '4':
                self._undo_ui()
            elif option == '5':
                return
            else:
                print("wrong option added")

#ui = BooksUI()
#ui.start()