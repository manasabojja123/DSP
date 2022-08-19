Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={"name":"manasa","age":18,"id":180122}
>>> len(d)
3
>>> type(d)
<class 'dict'>
>>> c=dict("name":"praveen","age":19,"id":180221}
SyntaxError: invalid syntax
>>> c=dict([("name","age","id"),("praveen",19,180221)])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c=dict([("name","age","id"),("praveen",19,180221)])
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> help(d)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> d["name"]="ruchitha
SyntaxError: EOL while scanning string literal
>>> d["name"]="ruchitha"
>>> print(d)
{'name': 'ruchitha', 'age': 18, 'id': 180122}
>>> d["gender"]="female"
>>> print(d)
{'name': 'ruchitha', 'age': 18, 'id': 180122, 'gender': 'female'}
>>> d.get("name")
'ruchitha'
>>> d.keys()
dict_keys(['name', 'age', 'id', 'gender'])
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.popitem()
('gender', 'female')
>>> print(d)
{'name': 'ruchitha', 'age': 18, 'id': 180122}
>>> d["marks"]=100
>>> print(d)
{'name': 'ruchitha', 'age': 18, 'id': 180122, 'marks': 100}
>>> d.pop("marks")
100
>>> print(d)
{'name': 'ruchitha', 'age': 18, 'id': 180122}
>>> d.values()
dict_values(['ruchitha', 18, 180122])
>>> d.items()
dict_items([('name', 'ruchitha'), ('age', 18), ('id', 180122)])
>>> d.keys()
dict_keys(['name', 'age', 'id'])
>>> print(d["age"])
18
>>> 
>>> del(d["age"])
>>> print(d)
{'name': 'ruchitha', 'id': 180122}
>>> d.copy()
{'name': 'ruchitha', 'id': 180122}
>>> d["marks"]=90
>>> d["gender"]="female"
>>> print(d)
{'name': 'ruchitha', 'id': 180122, 'marks': 90, 'gender': 'female'}
>>> d.copy()
{'name': 'ruchitha', 'id': 180122, 'marks': 90, 'gender': 'female'}
>>> dict.fromkeys(d)
{'name': None, 'id': None, 'marks': None, 'gender': None}
>>> dict.fromkeys(d,"hello")
{'name': 'hello', 'id': 'hello', 'marks': 'hello', 'gender': 'hello'}
>>> 
