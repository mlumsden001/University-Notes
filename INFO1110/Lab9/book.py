class Book:
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url

    def __str__(self):
        return "'{}'', a book by {} ({:.d}) [{}]".format(self.title, self.author, self.year, self.url)

    def how_old(self):
        return 2019 - self.year

book = Book("The Very Hungry Caterpillar", "Eric Carle", 1969, "www.tvhc.com")
