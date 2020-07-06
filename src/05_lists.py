# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print("1:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x = x + y
print("2:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
del x[x.index(8)]
print("3:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print("4:", x)

# Print the length of list x
print("5: Length ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
output = [item*1000 for item in x]
print("6:", output)