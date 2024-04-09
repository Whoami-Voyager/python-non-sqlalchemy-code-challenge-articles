class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title'):
            self._title = value
        else:
            print("not valid title")

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            print("not valid author")

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            print("not valid magazine")
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, 'name') and len(value) > 0:
            self._name = value
        else:
            print("not a valid name")

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({author.magazine for author in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})


class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print ("not valid name")

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print("incorrect category")

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({contributor.author for contributor in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [articles.title for articles in self.articles()]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        if contributing_authors:
            return contributing_authors 
        else:
             None


