from add_new_book import  add_new_book
from delete_book import delete_book
from read_book_list import  read_book_list
from update_book import update_book

book_list = []

while True:
    print('Welcome To Library Management System!!')
    print('0. Exit')
    print('1. Add A Book')
    print('2. Update A Book')
    print('3. Delete A Book')
    print('4. View All Books')

    option = input('\nChoose An Option: ')

    if option == '0':
        print('\n----------------------------------------')
        print('EXITING LIBRARY MANAGEMENT SYSTEM')
        print('----------------------------------------\n')

        print('Thank You For Using Library Management System!!\n')
        break

    elif option == '1':
        add_new_book()

    elif option == '2':
        update_book()

    elif option == '3':
        delete_book()

    elif option == '4':
        print('\n---------------------------')
        print('VIEW ALL BOOKS')
        print('---------------------------\n')

        book_list = read_book_list()

        if len(book_list):
            for index, book in enumerate(book_list, 1):
                print(f'{index}. Title: {book['title']} | Author(s): {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}')
        else:
            print('No Books Found!!')

        print('\n')
    else:
        print('Please, Select A Valid Option!!\n')