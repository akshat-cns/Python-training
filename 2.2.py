books = []

def show_menu():
    print(''' \nLibrary Menu:
    1. Add a book
    2. Remove a book
    3. Search for a book
    4. List all books
    5. Exit ''')

while True:
    show_menu()
    choice = input("Please choose an option (1-5): ")
    if choice == '1':
        book_name = input("Enter the name of the book to add: ")
        books.append(book_name)
        print(f'Book "{book_name}" added successfully.')

    elif choice == '2':
        book_name = input("Enter the name of the book to remove: ")
        if book_name in books:
            books.remove(book_name)
            print(f'Book "{book_name}" removed successfully.')
        else:
            print(f'Error: Book "{book_name}" not found in the library.')

    elif choice == '3':
        book_name = input("Enter the name of the book to search for: ")
        if book_name in books:
            print(f'Book "{book_name}" is in the library.')
        else:
            print(f'Error: Book "{book_name}" not found in the library.')

    elif choice == '4':
        if len(books) == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in books:
                print(f'- {book}')

    elif choice == '5':
        print("Exit!")
        break

    else:
        print("Invalid choice.")