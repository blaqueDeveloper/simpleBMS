# WEEK FOUR PHASE 3 PROJECT

## TITLE AND DESCRIPTION

### TITLE
BOOK MANAGEMENT SYSTEM

### DESCRIPTION
This is a comprehensive Book Management System (BMS) designed to help book enthusiasts, librarians, and collectors efficiently organize and manage their book collections. 



Here is an overview of how the interface works:

1. Book Cataloging: 

    <strong>Description:</strong> Users can easily add new books to the system by providing book title and the author.
    
    <strong>Process:</strong> To add a book, users access the "Add Book" feature, where they input the book's information into a user-friendly form. The system validates the data and stores it in the database.

2. Search Functionality: 

    <strong>Description:</strong> The BMS includes robust search capabilities, enabling users to find specific books quickly based on title or auhtor.

    <strong>Process:</strong> To search for a book, users types their search criteria. The system returns matching results, making it easy to locate specific books within the collection.

3. Display Books: 

    <strong>Description:</strong> Users have access to a comprehensive list of all the books in the collection.

    <strong>Process:</strong> Users can view the complete catalog of books by selecting the "Display All Books" option. The system presents the books in a user-friendly interface, allowing users to scroll through and explore the collection.

4. Add Comments: 

    <strong>Description:</strong> Users can contribute comments and reviews to books within the collection, sharing their thoughts and opinions with others.

    <strong>Process:</strong> To add a comment, users select a book and access the "Add Comment" feature. They can write and submit their comments, which are then associated with the respective book, creating a valuable resource for readers and recommendations.

5. Remove a Book:

    <strong>Description:</strong> The system allows authorized users to remove books from the collection when necessary, ensuring an up-to-date catalog.

    <strong>Process:</strong> To remove a book, authorized personnel access the "Remove Book" feature, select the book to be removed, and confirm the action. The system updates the catalog accordingly.

Overall, The Book Management System provides a user-friendly and efficient platform for managing and interacting with a book collection. Whether you're looking to add new books, explore the existing catalog, find a specific title, share your insights through comments, or perform maintenance tasks like book removal, the BMS simplifies these operations to enhance the overall book management experience.

This system is designed to streamline the organization and management of your personal or professional book collection. Whether you're an avid reader, a collector, or a librarian, Bookshelf Pro offers a powerful yet user-friendly command-line interface (CLI) to help you catalog, search, and maintain your book library with ease.



## TABLE OF CONTENT

### User Stories
As a user, I am able to do the following:-

1. See the a menu describing all the actions available
2. Add a new book by entering the title and the author
3. Display all books, their titles, their respective authors and the comments on each book
4. Look up a book by the book title or author
5. Add a comment to a book
6. Remove a book
7. Exit the interface


### Tech Stack
The following technologies were used to make this project a success:-

1. SQLALCHEMY

It provides a high-level, Object-Relational Mapping (ORM) and SQL toolkit for working with relational databases. It allows you to interact with databases in a more Pythonic way by abstracting many of the low-level details of working with SQL and database connections.

2. PYTHON

Python is a general-purpose programming language, which means it can be used for a wide range of applications, including web development, data analysis, machine learning, scripting, automation, scientific computing, and more.

3. ALEMBIC

This is an open-source database migration tool for Python. It is often used in conjunction with SQLAlchemy, the Python SQL toolkit and Object-Relational Mapping (ORM) library, to manage database schema changes and versioning. Alembic helps developers keep their database schema in sync with their application code as it evolves over time.


### Configuration
<strong>pipenv install</strong> 
To install dependencies

<strong>pipenv shell</strong>
To run the virtual encironment

<strong>pipenv install alembic</strong>
To install alembic

<strong>alembic init migrations</strong>
Where my migrations files will be stored

Navigate to the <strong>alemib.ini</strong> file and change the name of the data base.

Navigate to <strong>env.py</strong> file and import base


### Application
To run this interface, use the following commands in main folder:
1. Run <strong>python -m SQL.seed</strong>
To seed your database with random entries

2. Run <strong>python -m CLI.menu</strong>
This will display a menu that allows you to interact with the system.





## OWNERSHIP

### AUTHOR
The owner of this project is Dorine Watene Manyara.

### LICENSE 
This project is licensed under the MIT License. See <a href='https://choosealicense.com/licenses/mit/'>MIT</a> file for details.
