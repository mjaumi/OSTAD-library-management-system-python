from save_book_list import save_book_list

def add_new_book():
    # taking input to add new book here
    title = input("Enter Book's Title: ")
    author = input("Enter Book's author Name: ")
    isbn = input("Enter Book's ISBN Number: ")
    year = input("Enter Book's Publishing Year: ")
    price = float(input("Enter Book's Price: "))
    quantity = int(input("Enter Book's Quantity: "))

    # creating book list here
    book = [title, author, isbn, year, price, quantity]

    # calling function to save the book in a CSV file here
    save_book_list(book)