class Book:
    def _init_(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def royalty(self):
        return self._royalty

    @royalty.setter
    def royalty(self, royalty):
        self._royalty = royalty

    def calculate_royalty(self, copies_sold):
        if copies_sold <= 500:
            return 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            return 0.10 * self._price * 500 + 0.125 * self._price * (copies_sold - 500)
        else:
            return (0.10 * self._price * 500 + 
                    0.125 * self._price * 1000 + 
                    0.15 * self._price * (copies_sold - 1500))

    def royalty(self, copies_sold):
        self._royalty = self.calculate_royalty(copies_sold)
        return self._royalty


class EBook(Book):
    def _init_(self, title, author, publisher, price, format):
        super()._init_(title, author, publisher, price)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format):
        self._format = format

    def calculate_royalty(self, copies_sold):
        base_royalty = super().calculate_royalty(copies_sold)
        gst_deduction = base_royalty * 0.12
        return base_royalty - gst_deduction

    def royalty(self, copies_sold):
        self._royalty = self.calculate_royalty(copies_sold)
        return self._royalty


# Example usage:
book = Book("Sample Book", "John Doe", "Sample Publisher", 20)
ebook = EBook("Sample EBook", "Jane Doe", "Sample Publisher", 15, "EPUB")

print(f"Book royalty for 2000 copies: {book.royalty(2000)}")
print(f"EBook royalty for 2000 copies: {ebook.royalty(2000)}")