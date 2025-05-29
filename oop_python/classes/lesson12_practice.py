class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book) #we don't use self.book because that's not 
                                #defined with Library's constructor
#mistake 1: you attempted to iterate over a data structure whose structure you were shriking (by removing items from the list)
#mistake 2: you failed to acknowledge that the label, which is what is passed as an input to the method, is not the property that you were looking for to cross-check
#mistake 3: You did not undestand that the list was of labels (references to objects of the Book class) and that accessing their properties took iteration over the labels plus fetching them 
    def remove_book(self, book):
        tmp_list =[]
        current_title = (book.title)
        current_author = (book.author)
        for i in range(0, len(self.books)):
            if (current_author == self.books[i].author) and (current_title == self.books[i].title):
                tmp_list.append(self.books[i])
        for book in tmp_list:
            if book in self.books:
                self.books.remove(book)
        
        

    def search_books(self, search_string):
        #here, every book in self.books refers to an instance (or object) of
        #Book type with title and author properties. These properties may be
        #accessed, as they are, with the .title or .author properties. 
        found_books = []
        for book in self.books:
            #for visuals, self.books looks like: [book1, book2, book3...]
            current_title = (book.title).lower() #
            current_author = (book.author).lower() #
            #current_title_list = current_title.split()
            #current_author_list = current_author.split()
            small_search_string = search_string.lower() #
            #The commented line below has an issue: "or" evaluates for any string so long as it's not empty
            #if small_search_string in (current_author or current_title):
            if (small_search_string == current_author) or (small_search_string in current_title):
                found_books.append(book)
            #Can't be used to troubleshoot since "return" exits the loops.
#            else:
#                return print("Incorrect input. Try again.")
        
        return found_books
book1 = Book("The Trial","Franz Kafta")
library1 = Library("janes_library")
library1.add_book(book1)
print(library1.books) #this also prints the location of the book1 object (as Class Book)
print(library1.search_books("OI"))
"""
print(library1.books.book1.title) --> doesn't work because "books" is a list, not an object
print(library1.books[0]) --> this works to print the "book1" object reference
as a Book object and the properties of book1.
Therefore, we may conclude that "book1" is just a label. It's useful only to keep
code cleaner, but it has no use on the back-end process-thinking of Python. It
is simply a label to a pointer in the memory that stores the properties of the
instance of Book, in this case Book("The Trial", "Franz Kafka").
The same is true for "library1".
Note: you may refer to the label in the code, which is useful, but that's about
all that library1 or book1 does. So you can use "del library1" or
"for book in library1.books". Still, "library1" is just the memory location for
the object you're trying to look into (like <__main__.Library object at 0x...>)
"""
