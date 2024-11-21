import csv

# function to mutate the existing book list into the CSV file declared here
def mutate_book_list(book_list):
    # CSV file field names declared here
    field_names = ['Title', 'Author', 'ISBN', 'Year', 'Price', 'Quantity']

    updated_book_list = []

    for book in book_list:
        updated_book_list.append(book.values())

    try:
        with open('books_db.csv', 'w', newline='') as books_db_file:
            writer = csv.writer(books_db_file)

            writer.writerow(field_names)
            writer.writerows(updated_book_list)
    except Exception as e:
        print('Something Went Wrong While Mutating The Book List!!\n')