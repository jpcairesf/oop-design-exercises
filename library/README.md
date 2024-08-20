# Library Exercise

A library is an organized collection of books where members can borrow and return books. The library system keeps track of the books available, the members registered, and which books are borrowed by which members.

## Features
The library should be able to perform the following operations:

1. **Add Book**: Add a new book to the library's collection with an ISBN, title, and author.
2. **Create Member**: Register a new member with a unique name and member ID.
3. **Lend Book**: Allow a registered member to borrow a book if it's available.
4. **Return Book**: Allow a member to return a borrowed book, making it available again.
5. **Check Availability**: Check if a specific book is available in the library.
6. **Get Borrowed Books**: Retrieve a list of books currently borrowed by a specific member.

## Conditions
1. **Book**:
    - Each book must have a unique ISBN.
    - A book can either be available or borrowed.

2. **Member**:
    - Each member must have a unique member ID.
    - Members can borrow multiple books, but a book cannot be borrowed by more than one member at a time.

3. **Lending and Returning**:
    - A book must be available to be borrowed.
    - A book must be borrowed before it can be returned.
    - Borrowing and returning operations should update the book's availability status.
