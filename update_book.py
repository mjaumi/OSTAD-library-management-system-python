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
                option = input("Would You Like To Update The Book's Title? (y/n): ")

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
                option = input("Would You Like To Update The Book's Author(s)? (y/n): ")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    author_list = book['author'].split(', ')

                    while True:
                        for index, author in enumerate(author_list, 1):
                            print(f'{index}. {author}')

                        print(f'{len(author_list) + 1}. Add New Author')
                        try:
                            option = int(input('\nChoose An Option: '))

                            if option <= len(author_list):
                                while True:
                                    print("\n1. Update Author's Name")
                                    print("2. Delete Author's Name")

                                    choice = input('\nChoose An Option: ')

                                    if choice == '1':
                                        updated_author = input("Enter The Book's Updated Author: ")
                                        author_list[option - 1] = updated_author
                                        break

                                    elif choice == '2':
                                        del author_list[option - 1]
                                        print("\nAuthor's Name Deleted!!\n")
                                        break

                                    else:
                                        print('\nPlease, Select A Valid Option!!')
                                        continue

                            elif option == len(author_list) + 1:
                                new_author = input("Enter The Book's New Author: ")
                                author_list.append(new_author)

                            else:
                                print('Please, Select A Valid Option!!\n')
                                continue

                        except Exception as e:
                            print('Please, Select A Valid Option!!\n')
                            continue

                        break

                    book['author'] = ', '.join(author_list)

                    break
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Publishing Year? (y/n): ")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    try:
                        new_year = int(input("Enter The Book's Updated Publishing Year: "))
                        book['year'] = new_year
                        break
                    except Exception as e:
                        print('\nInvalid Publishing Year Input!!\n')
                        continue
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Price? (y/n): ")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    try:
                        new_price = float(input("Enter The Book's Updated Price: "))
                        book['price'] = new_price
                        break
                    except Exception as e:
                        print('\nInvalid Price Input!!\n')
                        continue
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            while True:
                option = input("Would You Like To Update The Book's Quantity? (y/n): ")

                if option.lower() == 'n':
                    break
                elif option.lower() == 'y':
                    try:
                        new_quantity = int(input("Enter The Book's Updated Quantity: "))
                        book['quantity'] = new_quantity
                        break
                    except Exception as e:
                        print('\nInvalid Quantity Input!!\n')
                        continue
                else:
                    print('Please, Select A Valid Option!!\n')
                    continue

            mutate_book_list(book_list)
            print('\nBook Updated Successfully!!\n')
            return

    print('\nNo Book Found Containing The Given ISBN Number!!\n')