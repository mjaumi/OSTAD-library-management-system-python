from add_new_book import  add_new_book

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

    else:
        print('Please, Select A Valid Option!!')