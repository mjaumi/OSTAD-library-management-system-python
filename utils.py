# function to convert book list data to dictionary declared here
def convert_list_to_dictionary(book_list_data):
    field_names = book_list_data[0]
    book_list = []

    for book in book_list_data[1:]:
        book_dic = {}
        for i in range(0, len(book)):
            book_dic[field_names[i].lower()] = book[i]

        book_list.append(book_dic)

    return book_list
