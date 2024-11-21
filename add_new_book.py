from read_book_list import read_book_list
from save_new_book import save_new_book

def add_new_book():
    print('\n---------------------------')
    print('ADD NEW BOOK')
    print('---------------------------\n')

    try:
        authors = []

        # taking input to add new book here
        title = input("Enter Book's Title: ")
        authors.append(input("Enter Book's author Name: "))

        # taking multiple author names as input here
        while True:
            option = input('Want To Add More Authors? (y/n): ')

            if option.lower() == 'n':
                break
            elif option.lower() == 'y':
                authors.append(input("Enter Book's author Name: "))
            else:
                print('Please, Select A Valid Option!!\n')

        isbn = input("Enter Book's ISBN Number: ")
        year = input("Enter Book's Publishing Year: ")
        price = float(input("Enter Book's Price: "))
        quantity = int(input("Enter Book's Quantity: "))

        book_list = read_book_list()

        # making sure the uniqueness of the ISBN here
        if len(book_list):
            for book in book_list:
                if book['isbn'] == isbn:
                    print('\nBook With Similar ISBN Already Exists!!\n')
                    return

        # creating book list here
        book = [title, ', '.join(authors), isbn, year, price, quantity]

        # calling function to save the book in a CSV file here
        save_new_book(book)

    except Exception as e:
        print('\nInvalid Input!!\n')