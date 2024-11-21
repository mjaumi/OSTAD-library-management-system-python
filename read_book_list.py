import csv

# function to read all the books from CSV file declared here
def read_book_list(book_list):
    try:
        with open('books_db.csv', 'r') as books_db_file:
            reader = csv.reader(books_db_file)

            for row in reader:
                book_list.append(row)

        # returning only books except the field name here
        return book_list[1:]

    except Exception as e:
        print('Something Went Wrong While Reading All The Books!!\n')
