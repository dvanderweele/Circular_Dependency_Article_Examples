

# Base.py 

class Base:
  def getChildType(self):
    from ._index import registry
    return registry[self.__class__.hasMany]
  def getOwnerType(self):
    from ._index import registry
    return registry[self.__class__.belongsTo]