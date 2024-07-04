class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <=50):
            raise TypeError("Article title must be a string between 5 and 50 characters long")
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Author name must be a string and not empty")
        self._name = name

    @property
    def name(self):
         return self._name

    
    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise TypeError("Magazine name must be a string between 2 and 16 characters long")
        if not isinstance(category, str) or len(category) == 0:
            raise TypeError("Magazine category must be a string and not empty")
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass