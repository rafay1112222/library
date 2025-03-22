import json

def load_library(filename="library.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library, filename="library.json"):
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_books(library):
    choice = input("Search by: 1. Title 2. Author\nEnter choice: ")
    query = input("Enter search term: ").lower()
    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    if matches:
        for book in matches:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("No books in the library.")
        return
    for book in library:
        status = "Read" if book["read"] else "Unread"
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    print(f"Total books: {total_books}")
    print(f"Percentage read: {100 * read_books / total_books:.2f}%")

def main():
    library = load_library()
    while True:
        print("\nMenu:\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
