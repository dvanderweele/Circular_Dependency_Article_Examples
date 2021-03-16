

# MyClass.py 

class MyClass:
  # class attribute
  numInstances = 0
  # instance constructor
  def __init__(self):
    self.__class__.numInstances += 1
  # instance destructor
  def __del__(self):
    self.__class__.numInstances -= 1