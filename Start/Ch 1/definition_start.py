# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  # The init fn is one of python's special functions for working with classes. When
  # a class is created, the init function is then called to initialize the new object
  # with information and it is called before any other functions that we may have 
  # defined in th class. This is an INITIALIZER function rather than a CONSTRUCTOR.
  # The reason is that at the point of calling this function, the object has already
  # been created.
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
# Although the init method takes two arguments, we've only supplied one because
# whenever we call a method on a Python object, the object itself automatically gets
# passed as the first argument. Also, the word 'self' is just a convention. It can
# be called anything. The object is constructed by calling the class name followed by 
# parentheses and, optionally, values to be passed to the object as shown below.
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title)