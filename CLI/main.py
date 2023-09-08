import argparse
from books import BookApp
from SQL import models

def main():
    parser = argparse.ArgumentParser(description="BOOKS MANAGEMENT SYSTEM")
    parser.add_argument("-a", "--add", help="Add a book to the list (provide title and author as 'Title, Author')")
    parser.add_argument("-l", "--look", help="Look if a book exists")
    parser.add_argument("-d", "--display", action="store_true", help="Display all books")
    parser.add_argument("-c", "--comment", type=int, help="Add a comment to a specific book by index")
    parser.add_argument("-r", "--remove", type=int, help="Remove a book from the system")
    args = parser.parse_args()

    app = BookApp()

    if args.add:
        title, author = args.add.split(',')
        
        # Create a new book record in the database.
        author_obj = models.Author(name=author.strip())
        book_obj = models.Book(title=title.strip(), author=author_obj)
        
        app.add_book(book_obj)
    elif args.look:
        result = app.look_up_book(args.look)
        print(result)
    elif args.display:
        print(app.read_books())
    elif args.comment:
        index = args.comment
        comment_text = input("Enter your comment: ")
        result = app.add_comment_to_book(index, comment_text)
        print(result)
    elif args.remove:
        print(app.remove_book(args.remove))
    else:
        print("Enter a valid command!")

if __name__ == "__main__":
    main()
