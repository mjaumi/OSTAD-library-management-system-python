# title, author(s), ISBN, publishing year, price, and quantity

def add_new_book():
    # taking input to add new book here
    title = input("Enter Book's Title: ")
    author = input("Enter Book's author Name: ")
    isbn = input("Enter Book's ISBN Number: ")
    year = input("Enter Book's Publishing Year: ")
    price = float(input("Enter Book's Price: "))
    quantity = int(input("Enter Book's Quantity: "))

    # creating book dictionary here
    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'year': year,
        'price': price,
        'quantity': quantity
    }