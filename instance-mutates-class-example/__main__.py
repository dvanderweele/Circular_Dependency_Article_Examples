

# __main__.py 

from .MyClass import MyClass 

def numObjects():
  print(f'Number of instances of MyClass: {MyClass.numInstances}')

numObjects()

print('Instantiating 3 MyClass objects...')

x = [MyClass() for i in range(0,3)]

numObjects()

print('Deleting 1 of the MyClass objects...')

del x[2]

numObjects()

print('Deleting the remaining two instances...')

del x[1]
del x[0]

numObjects()