#!/usr/bin/python3
#!/usr/bin/python3

# Import the Rectangle class from a module named '1-rectangle'
Rectangle = __import__('1-rectangle').Rectangle

# Create an instance of the Rectangle class with dimensions 2x4
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

# Modify the width and height attributes of the rectangle
my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
