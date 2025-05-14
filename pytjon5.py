# Base class representing a Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._pages = pages             # Protected attribute (by convention)

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    def read_sample(self):
        return f"Reading a sample of '{self.title}'..."

# Derived class representing an EBook, inherits from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb, format_type):
        super().__init__(title, author, pages)
        self.__file_size_mb = file_size_mb   # Private attribute
        self.format_type = format_type        # Public attribute

    def get_info(self):
        # Override to include format and file size
        info = super().get_info()
        return f"{info} Format: {self.format_type}, Size: {self.__file_size_mb}MB."

    def read_sample(self):
        # Polymorphism: different implementation
        return f"Opening '{self.title}' in {self.format_type} format..."

    def get_file_size(self):
        return f"{self.__file_size_mb} MB"

