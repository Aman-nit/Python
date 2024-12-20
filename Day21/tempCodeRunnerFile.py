
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(p3.x, p3.y) # prints 4, 6
# How to overload an operator in Python?
# You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:

# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# < : __lt__
# > : __gt__
# == : __eq__
# For example, if you want to overload the + operator to add two instances of a custom class, you would define the add method:
