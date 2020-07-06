"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("Hello, my name is John. I am %i years old. %s and this is Pedro my turtle, he is %2f years old!" % (x, z, y))
# Use the 'format' string method to print the same thing
print(f"Hello, my name is John. I am {x} years old. {z} and this is Pedro my turtle, he is {y} years old!")

my_string = "Hello, my name is John. I am {} years old. {} and this is Pedro my turtle, he is {} years old!"
  
print (my_string.format(x, z, y)) 