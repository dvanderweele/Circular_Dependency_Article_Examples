

# classDefiner.py 

def defineClassesInOrder(order):
  defined = []
  orderIndex = 0
  while len(defined) < 3:
    if order[orderIndex] == 1:
      class ClassA:
        def __str__(self):
          return "I'm ClassA."
      defined.append(ClassA)
    elif order[orderIndex] == 2:
      class ClassB:
        def __str__(self):
          return "I'm ClassB."
      defined.append(ClassB)
    elif order[orderIndex] == 3:
      class ClassC:
        def __str__(self):
          return "I'm ClassC."
      defined.append(ClassC)
    orderIndex += 1
  return defined[0], defined[1], defined[2]