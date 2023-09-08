import random
from faker import Faker
from SQL.models import Author, Book, Comment, Reader
from SQL.main import session

fake = Faker()

# Generate random book titles and authors
def generate_random_data(num_entries):
    for _ in range(num_entries):
        title = fake.catch_phrase()
        author_name = fake.name()

        # Check if the author already exists in the database, if not, add them
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            session.add(author)
            session.commit()

        book = Book(title=title, author=author)
        session.add(book)
        session.commit()

        # Generate random reader name and create a reader
        reader_name = fake.name()
        reader = Reader(name=reader_name)
        session.add(reader)
        session.commit()

        # Add a random comment for each book associated with the reader
        comment_text = fake.paragraph()
        comment = Comment(text=comment_text, book=book, reader=reader)
        session.add(comment)
        session.commit()

if __name__ == "__main__":
    num_entries = 20  # Adjust the number of entries you want to generate
    generate_random_data(num_entries)
    print(f"Generated and added {num_entries} random books with comments and readers to the database.")
