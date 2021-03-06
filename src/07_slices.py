"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[4])

# Output the last three elements in the array: [7, 9, 6]
b = [7, a[4], 6]
print(b[:3])

# Output the two middle elements in the array: [1, 7]
c = [1, b[0]]
print(c[0:2])

# Output every element except the first one: [4, 1, 7, 9, 6]
d = [a[1], c[0], b[0], a[4], b[2]]
print(d[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
e = [2, a[1], c[0], b[0], a[4],]
print(e[:len(e)-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])