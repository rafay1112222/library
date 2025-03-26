import streamlit as st
import json

# Function to load the library from a JSON file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save the library to a JSON file
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Load library data
library = load_library()

# Streamlit App Title
st.title("📚 Personal Library Manager")

# Navigation (Tabs)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Add Book", "❌ Remove Book", "🔎 Search Books", "📚 View Library", "📊 Statistics"])

# Tab 1: Add a Book
with tab1:
    st.header("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    read_status = st.checkbox("I have read this book")

    if st.button("Add Book"):
        if title and author and year and genre:
            new_book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
            library.append(new_book)
            save_library(library)
            st.success(f"✅ '{title}' has been added!")
        else:
            st.error("⚠️ Please fill in all fields!")

# Tab 2: Remove a Book
with tab2:
    st.header("Remove a Book")
    book_titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove", book_titles, index=None, placeholder="Select a book")

    if st.button("Remove Book"):
        if book_to_remove:
            library = [book for book in library if book["title"] != book_to_remove]
            save_library(library)
            st.success(f"❌ '{book_to_remove}' has been removed!")
        else:
            st.error("⚠️ Please select a book to remove!")

# Tab 3: Search Books
with tab3:
    st.header("Search for a Book")
    search_query = st.text_input("Enter title or author")

    if st.button("Search"):
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for book in results:
                status = "✅ Read" if book["read"] else "📖 Unread"
                st.write(f"📚 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("❌ No matching books found.")

# Tab 4: Display All Books
with tab4:
    st.header("Your Library")
    if library:
        for book in library:
            status = "✅ Read" if book["read"] else "📖 Unread"
            st.write(f"📚 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("📂 No books in your library yet.")

# Tab 5: Library Statistics
with tab5:
    st.header("Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])

    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
        st.write(f"📚 **Total Books:** {total_books}")
        st.write(f"✅ **Books Read:** {read_books} ({read_percentage:.2f}%)")
    else:
        st.warning("📂 No books in your library yet.")
