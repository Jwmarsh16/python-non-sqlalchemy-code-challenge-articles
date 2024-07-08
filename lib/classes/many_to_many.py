class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author  
        self.magazine = magazine  
        self.title = title  
        if self not in author._articles:
            author._articles.append(self)
        if self not in magazine._articles:
            magazine._articles.append(self)
        self.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title') and isinstance(value, str) and (5 <= len(value) <= 50):
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):    
            self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name  
        self._articles = [] 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') and isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self._articles) == 0:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        self.name = name  
        self.category = category  
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value
        
        

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in self._articles if isinstance(article, Article)]

    def contributors(self):
        return list({article._author for article in self._articles if isinstance(article, Article)})

    def article_titles(self):
        if len(self._articles) == 0:
            return None
        else:
            return [article._title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article._author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
            
