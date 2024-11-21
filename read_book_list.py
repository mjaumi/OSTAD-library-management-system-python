import csv
from utils import convert_list_to_dictionary


# function to read all the books from CSV file declared here
def read_book_list():
    try:
        books_db_data = []

        with open('books_db.csv', 'r') as books_db_file:
            reader = csv.reader(books_db_file)

            for row in reader:
                books_db_data.append(row)

        book_list = convert_list_to_dictionary(books_db_data)

        return book_list

    except Exception as e:
        print('Something Went Wrong While Reading All The Books!!\n')
