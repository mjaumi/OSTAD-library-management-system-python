from mutate_book_list import mutate_book_list
from read_book_list import read_book_list

# function to delete books from CSV file declared here
def delete_book():
    print('\n---------------------------')
    print('DELETE BOOK')
    print('---------------------------\n')

    isbn = input("Enter The Book's ISBN You Want To Delete: ")

    # fetching the book list from CSV file here
    book_list = read_book_list()

    for book in book_list:
        if book['isbn'] == isbn:
            book_list.remove(book)
            mutate_book_list(book_list)
            print('Book Deleted Successfully!!\n')
            return

    print('No Book Found Containing The Given ISBN Number!!\n')