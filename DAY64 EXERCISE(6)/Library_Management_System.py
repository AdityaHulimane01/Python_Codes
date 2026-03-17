class Library:
    no_of_Books = 0
    Books = []

    def insertBooks(self):
        book = input("Enter the Book name : ")
        Library.Books.append(book)
        Library.no_of_Books += 1
        
lib1 = Library()
lib1.insertBooks()

print(Library.Books)
print("Total Books:", Library.no_of_Books)

