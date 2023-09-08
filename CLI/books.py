import json
from SQL.models import Author, Book, Comment
from SQL.main import session
from sqlalchemy.orm import joinedload


class BookApp:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file, indent=2)

    def add_book(self, book):
        session.add(book)
        session.commit()
        print(f'BOOK SUCCESSFULLY ADDED!.')


    def read_books(self):
        books = session.query(Book).all()
        library = "BOOK MANAGEMENT SYSTEM\n"

        for i, book in enumerate(books, start=1):
            library += f'{i}. Title: {book.title}, Author: {book.author.name}\n'

            # Fetch and display comments for the book
            comments = session.query(Comment).filter_by(book_id=book.id).all()
            if comments:
                library += "   Comments:\n"
                for comment in comments:
                    library += f"   - {comment.text}\n"

        return library


    def look_up_book(self, query):
        books = session.query(Book).join(Author).filter(
        (Book.title.ilike(f"%{query}%")) | (Author.name.ilike(f"%{query}%"))
        ).all()

        if not books:
            return "No matching books found"

        result = "Matching books:\n"
        for i, book in enumerate(books, start=1):
            result += f'{i}. Title: {book.title}, Author: {book.author.name}\n'

        return result

    def add_comment_to_book(self, index, reader_name):
        books = session.query(Book).all()

        if 1 <= index <= len(books):
            book = books[index - 1]

            # Prompt the reader for their comment
            comment_text = input("Enter your comment: ")

            # Create a new comment record in the database
            comment = Comment(text=comment_text, book=book, reader_name=reader_name)
            session.add(comment)
            session.commit()

            return f'Added comment to book: Title: {book.title}, Author: {book.author.name}'
        else:
            return "Invalid index"



    

    def remove_book(self, index):
        books = session.query(Book).all()

        if 1 <= index <= len(books):
            book = books[index - 1]

            # Load the book with its author before deletion
            book_with_author = session.query(Book).filter_by(id=book.id).options(joinedload(Book.author)).first()
            
            if book_with_author:
                deleted_book_title = book_with_author.title
                deleted_author_name = book_with_author.author.name

                # Remove the book from the database
                session.delete(book_with_author)
                session.commit()

                return f'Deleted book: Title: {deleted_book_title}, Author: {deleted_author_name}.'
        else:
            return "Invalid index"