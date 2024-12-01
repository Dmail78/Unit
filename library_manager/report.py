from .catalog import Library
from .utils import format_book_data

def generate_report(library:Library):
    res = []
    for book in library.books:
            res.append(format_book_data(book)+"\n")
    return "".join(res)