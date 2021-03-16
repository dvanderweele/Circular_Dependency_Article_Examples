

# _index.py 

from .Fembot import Fembot
from .Wile import Wile

registry = {
  'Fembot': Fembot,
  'Wile': Wile 
}