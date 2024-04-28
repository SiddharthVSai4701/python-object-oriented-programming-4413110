# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        # These are called instance attributes because the values are only held by
        # the instance of the object that it is declared on. The same goes for
        # instance methods.
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        # If we try to print this out by using an object we will get an error as it is not 
        # visible outside the class. However, it can be printed or accessed inside class methods.
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    # All instance methods take the object as the first argument
    def getprice(self):
        # We will use the discount if it is defined. Since it is not defined during
        # init, we can't rely on it being present. So, we test for it using the hasattr
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        # The underscore is to indicate to other developers that this attribute
        # is internal to the class and is not for public consumption.
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
# If we use a double underscore before a method name, the Python interpreter
# will change the name of that property so that other classes will get an error
# if they try to access it
