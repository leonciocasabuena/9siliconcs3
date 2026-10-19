class Publication: #Creates a class names Publication, which is the parent class of both the Book and Magazine class -- and will also be the source for the inherited attributes of the latter.
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("---Publication Information---")
        print(f"Title: {publication_1.get_title()}")
        print(f"Author: {publication_1.get_author()}")
        
class Book(Publication): #Creates a child class Book which inherits the title and author attributes of the parent class Publication using the super() function, while also having the ability to add additional indeppendent attributes. 
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = int(number_pages)
        self.set_number_pages(number_pages)
    
    def get_number_pages(self):
        return self.__number_pages

    def set_number_pages(self, number_pages):
        if number_pages<0:
            print("The number of pages shall be a positive number.")
        else:
            self.__number_pages = int(number_pages)
          
    def display_info(self):
        print("---Book Information---")
        print(f"Title: {book_1.get_title()}")
        print(f"Author: {book_1.get_author()}")
    
class Magazine(Publication): #Creates a child class Magazine which also inherits the title and author attributes of the parent class Publication using the super() function, while also having the ability to add additional indeppendent attributes.
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__number_pages = int(issue_number)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__number_pages

    def set_issue_number(self, issue_number):
        if issue_number<0:
            print("Issue number shall be a positive number.")
        else:
            self.__number_pages = int(issue_number)

    def display_info(self):
        print("---Magazine Information---")
        print(f"Title: {magazine_1.get_title()}")
        print(f"Author: {magazine_1.get_author()}")

#Instantiates three different objects from each classes mentioned above.
publication_1 = Publication("Pyramid Books", "Various Publicators") 
book_1 = Book("I Have No Mouth & I Must Scream", "Harlan Ellison", 14)
magazine_1 = Magazine("IF: Worlds of Science Fiction", "Various Authors", 112)

publication_1.display_info() #calls the display_info() function from the class Publication, which was configured earlier -- displaying both the title and the author of the publication.

print("")

book_1.set_number_pages(-14) #sets the number of pages to a value of -14, but then -- the function contains a restriction which prevents it from updating the new number of pages into a numerical digit less than or equal to zero -- therefore the program ignores the call and proceeds to the next line of code.
book_1.display_info() #also calls the display_info() function from the child class Book, which was also configured earlier -- displaying both the title and the author of the book.

print(f"Number of Pages: {book_1.get_number_pages()}") #calls the get_number_pages() function from the child class Book, and prints the given number of pages from the instantiated object.

print("")

magazine_1.set_issue_number(-112) #sets the issue number to a value of -122, but then -- the function also contains a restriction which prevents it from updating the new issue number into a numerical digit less than or equal to zero -- therefore the program ignores the call and proceeds to the next line of code.
magazine_1.display_info() #also calls the display_info() function from the child class Magazine, which was also configured earlier -- displaying both the title and the author of the magazine.
print(f"Issue Number: {magazine_1.get_issue_number()}") #calls the get_issue_number() function from the child class Magazine, and prints the given issue number from the instantiated object.
