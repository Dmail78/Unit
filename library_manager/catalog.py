from .utils import validate_book_data, format_book_data


class Library():
    def __init__(self) -> None:
        self.books = []
        
    def add_book(self, book:dict):
        if validate_book_data(book):
            self.books.append(book)
            print(f"Добавили книгу: {format_book_data(book)}")
            print()
        else:
            print(f"Данные о книге {book['name']} некорректны")
        
    def remove(self, name:str):
        temp = list(filter(lambda x: x["name"] == name, self.books))[0]
        del self.books[self.books.index(temp)]
        print(f"Удалили книгу: {format_book_data(temp)}")
        print()
    
    def view_books(self):
        print("Печать библиотеки")
        res = []
        for book in self.books:
            print(format_book_data(book))
        print()
        