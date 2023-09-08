from CLI.books import BookApp
from SQL.models import Author, Book

def display_menu():
    print("WELCOME TO YOUR BOOK MANAGEMENT SYSTEM")
    print("1. Add a book 📚")
    print("2. Display all books 📖")
    print("3. Look up a book 🔍")
    print("4. Add a comment to a book 💬")
    print("5. Remove a book 🗑️")
    print("6. Exit 🚪")
    print("Please enter a number to choose what you want to do")

def main():
    app = BookApp()

    while True:
        display_menu()
        choice = input()

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            author_obj = Author(name=author)  # Use the imported Author directly
            book_obj = Book(title=title, author=author_obj)  # Use the imported Book directly

            # Add the book to the database
            app.add_book(book_obj)
        elif choice == '2':
            print(app.read_books())
        elif choice == '3':
            query = input("Enter a title or author to search: ")
            result = app.look_up_book(query)
            print(result)
        elif choice == '4':
            index = int(input("Enter the index of the book to add a comment to: "))
            reader_name = input("Enter your name: ")
            result = app.add_comment_to_book(index, reader_name)
            print(result)
        elif choice == '5':
            index = int(input("Enter the index of the book to remove: "))
            result = app.remove_book(index)
            print(result)
        elif choice == '6':
            print("THANK YOU FOR USING THE BOOK MANAGEMENT SYSTEM! HAVE A GREAT DAY! 😊")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
