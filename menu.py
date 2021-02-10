from app import books
import logging

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''\nEnter one of the following:
- 'b' to look at 5 star books,
- 'c' to look at the cheapest books,
- 'n' to get the next available book on the page,
- 'q' to quit.

Enter your choice: '''

def menu():
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice == 'b':
            print_best_books()
        elif choice == 'c':
            print_cheapest_books()
        elif choice == 'n':
            print_next_book()
        else:
            print('Please choose a valid command.')

        choice = input(USER_CHOICE)
    logger.debug('Terminating program...')


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10] # * -1 makes it so we can sort descending
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (book for book in books)


def print_next_book():
    logger.info('Finding next book from generator of all books...')
    print(next(books_generator))


menu()