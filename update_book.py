from mutate_book_list import mutate_book_list
from read_book_list import read_book_list


def update_book():
    print('\n---------------------------')
    print('UPDATE BOOK')
    print('---------------------------\n')

    isbn = input("Enter The Book's ISBN You Want To Update: ")

    # fetching the book list from CSV file here
    book_list = read_book_list()

    for book in book_list:
        if book['isbn'] == isbn:
            while True:
                option = input("Would You Like To Update The Book's Title? (y/n)")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    new_title = input("Enter The Book's Updated Title: ")
                    book['title'] = new_title
                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Author(s)? (y/n)")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    author_list = book['author'].split(', ')
                    while True:
                        for index, author in enumerate(author_list, 1):
                            print(f'{index}. {author}')

                        print(f'{len(author_list) + 1}. Add New Author')

                        option = int(input('\nChoose An Option: '))

                        if option <= len(author_list):
                            updated_author = input("Enter The Book's Updated Author: ")
                            author_list[option - 1] = updated_author

                        elif option == len(author_list) + 1:
                            new_author = input("Enter The Book's New Author: ")
                            author_list.append(new_author)

                        book['author'] = ', '.join(author_list)
                        break

                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Publishing Year? (y/n)")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    new_year = input("Enter The Book's Updated Publishing Year: ")
                    book['year'] = new_year
                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Price? (y/n)")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    new_price = input("Enter The Book's Updated Price: ")
                    book['price'] = new_price
                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Quantity? (y/n)")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    new_quantity = input("Enter The Book's Updated Quantity: ")
                    book['quantity'] = new_quantity
                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            mutate_book_list(book_list)
            print('Book Updated Successfully!!\n')
            return

    print('No Book Found Containing The Given ISBN Number!!\n')