from library_books import library_books
from datetime import datetime, timedelta


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_books():
    print("Here is a list of all the books within our system at the moment")
    print("")
    #Goes through every book in the dictionary and prints the ID, Title, and Author
    for book in library_books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    print("")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive+
# Return a list of matching books

#https://www.w3schools.com/python/ref_string_lower.asp
#Used AI tool to learn a way to search more effectively, instead a multitiude of if statements
def search_books():
    #User input allows for them to search for either the Author or Genre
    search = str(input("Search Book by Author or Genre: ")).lower()
    #Goes through the books in the list and puts the ones that apply to search and put it in a seperate list
    results = [book for book in library_books
                if search in book['author'].lower() or search in book['genre'].lower()]
    print("")
    #Goes through all the books that were placed in results and prints the title, author, and genre
    for books in results:
        print(f"{books['title']}, {books['author']}, {books['genre']}")
    print("")

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# https://www.geeksforgeeks.org/python/how-to-add-and-subtract-days-using-datetime-in-python/
def checkout_book():
    #Goes through all the books and shows their ID, Title, and Availability
    for book in library_books:
        print(f"{book['id']}, {book['title']}, {book['available']}")
    print("")
    #Ask the user what book they want to check out by ID
    choice = input("Type the ID of the book you would like to checkout: ").upper()
    #Go through all the books in the library, if the id is the same as the user input and availability is true, change the availibilty, change the due date, and add a checkout
    for book in library_books:
        if choice == book['id']:
            if book['available']:
                book['available'] = False
                book['due_date'] = datetime.now() + timedelta(days = 14)
                book['checkouts'] += 1
                print("")
    #Print that the book was checked out and show the book that was checked out and all the updated info along with it
                print(f"The book has been checked out!")
                print(f"{book['id']}, {book['title']}, {book['available']}, {book['checkouts']}, {book['due_date']}")
                print("")
            else:
                print("The book is currently unavailable")
                print("")
    
   
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def book_return():
    #Goes through all the books in the library, printing each ones info
    for book in library_books:
        print(f"{book['id']}, {book['title']}, {book['available']}, {book['checkouts']}, {book['due_date']}")
    print("")
    #Ask the user what they want to return by ID
    choice = input("Type the ID of the book you would like to return: ").upper()
    #Go through each book, and if it is the same as the user input, and the availability is false, change the availabilty and due date
    for book in library_books:
        if choice == book['id']:
            if book['available'] == False:
                book['available'] = True
                book['due_date'] = "None"
                print("The book has been returned!")
                print("")
                print(f"{book['id']}, {book['title']}, {book['available']}, {book['checkouts']}, {book['due_date']}")
                print("")
            else:
                print("The book is not checked out")
                print("")

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

#Print all the different options and depending on the number inputted, run the correlating function.
def menu():
    while True:
        print("1. View our available books")
        print("2. Search the database")
        print("3. Checkout one of our book")
        print("4. Return a checked out book")
        print("5. Most checked out books")
        print("6. Exit")
        print("")
        option = int(input("Choose what you would like to do: "))
        if option == 1:
            view_books()
        elif option == 2:
            search_books()
        elif option == 3:
            checkout_book()
        elif option == 4:
            book_return()
        elif option == 5:
            top_three()
        elif option == 6:
            print("Thank you for visitng, Goodbye!")
            break



# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog

# - Sort and display the top 3 most checked-out books
# https://www.datacamp.com/tutorial/sort-a-dictionary-by-value-python
# https://www.w3schools.com/python/python_strings_slicing.asp
# https://www.youtube.com/watch?v=YT5gI9IUJRQ&t=23s


def top_three():
    print("These are the most checked out books!")
    print("")
    #Put the books in order by greatest amount of checkouts to least
    sort_books = sorted(library_books, key = lambda books: books['checkouts'], reverse = True)
    #Slice it to where only the first three are shown, then print the title and amount of checkouts.
    top3 = sort_books[:3]
    for books in top3:
        print(f"{books['title']}, {books['checkouts']}")
    print("")

# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!



if __name__ == "__main__":
    print("Welcome to the Library! What can I do for you today!")
    print("")
    menu()
