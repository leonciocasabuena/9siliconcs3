class Publication:
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
        
class Book(Publication):
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
    
class Magazine(Publication):
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

publication_1 = Publication("Pyramid Books", "Various Publicators")
book_1 = Book("I Have No Mouth & I Must Scream", "Harlan Ellison", 14)
magazine_1 = Magazine("IF: Worlds of Science Fiction", "Various Authors", 112)

publication_1.display_info()

print("")

book_1.set_number_pages(-14)
book_1.display_info()

print(f"Number of Pages: {book_1.get_number_pages()}")

print("")
magazine_1.set_issue_number(-112)
magazine_1.display_info()
print(f"Issue Number: {magazine_1.get_issue_number()}")
