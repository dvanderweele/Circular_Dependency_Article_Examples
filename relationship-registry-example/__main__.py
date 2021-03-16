

# __main__.py 

from .Fembot import Fembot 
from .Wile import Wile 

print('Fembots have many:')
print(Fembot().getChildType())
print('A single Wile may belong to only one:')
print(Wile().getOwnerType())