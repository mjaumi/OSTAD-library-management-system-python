from add_new_book import  add_new_book
from read_book_list import  read_book_list

book_list = []

while True:
    print('Welcome To Library Management System!!')
    print('0. Exit')
    print('1. Add A Book')
    print('2. Update A Book')
    print('3. Delete A Book')
    print('4. View All Books')

    option = input('Select An Option: ')

    if option == '0':
        print('Thank You For Using Library Management System!!\n')
        break

    elif option == '1':
        add_new_book()

    elif option == '4':
        book_list = read_book_list(book_list)

        for book in book_list:
            print(f'Title: {book[0]} | Author: {book[1]} | ISBN: {book[2]} | Year: {book[3]} | Price: {book[4]} | Quantity: {book[5]}\n')

    else:
        print('Please, Select A Valid Option!!')