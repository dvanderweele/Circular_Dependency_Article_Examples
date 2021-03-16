

# __main__.py 

from .classDefiner import defineClassesInOrder

# let's pretend the order of numbers in the following tuple is defined from user input (change the order if you like)
order = (2, 3, 1)

One, Two, Three = defineClassesInOrder(order)

print(One())
print(Two())
print(Three())