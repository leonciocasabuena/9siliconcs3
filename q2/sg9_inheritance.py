class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        
class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title)

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title)
