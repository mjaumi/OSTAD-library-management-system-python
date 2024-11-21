import os.path as path
import csv

# function to save newly added book into the CSV file declared here
def save_new_book(book):
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