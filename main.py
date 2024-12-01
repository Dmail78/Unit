from library_manager import Library
from library_manager import generate_report

lib = Library()
lib.add_book({'name':'Onegin', 'author':'Pushkin', 'genre':'roman'})
lib.add_book({'name':'OSultane', 'author':'Pushkin', 'genre':'fantastic'})
lib.add_book({'name':'Onegin1', 'author':'', 'genre':'roman'})
lib.view_books()
lib.remove('Onegin')
lib.view_books()
print("Генерация отчета:", "\n", generate_report(lib))