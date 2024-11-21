import os.path as path
import csv

# title, author(s), ISBN, publishing year, price, and quantity

def save_book_list(book):
    # CSV file field names declared here
    field_names = ['Title', 'Author', 'ISBN', 'Year', 'Price', 'Quantity']

    if path.isfile('books_db.csv'):
        try:
            with open('books_db.csv', 'a', newline='') as books_db_file:
                writer = csv.writer(books_db_file)
                writer.writerow(book)

            print('New Book Added Successfully!!\n')
        except Exception as e:
            print('Something Went Wrong While Adding The Book!!\n')

    else:
        try:
            with open('books_db.csv', 'w', newline='') as books_db_file:
                writer = csv.writer(books_db_file)
                writer.writerow(field_names)
                writer.writerow(book)

            print('New Book Added Successfully!!\n')
        except Exception as e:
            print('Something Went Wrong While Adding The Book!!\n')