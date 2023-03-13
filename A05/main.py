from src.services.book_service import BookService
from src.ui.UI import BooksUI


def main():
    service = BookService()
    service.generate_books()
    ui = BooksUI(service)
    ui.start()


main()
