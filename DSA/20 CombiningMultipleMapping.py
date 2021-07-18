#Combining multiple mapping into a single mapping

from collections import ChainMap

a = {'x':1,'z':3}
b = {'y':2,'z':4}

c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))

d = list(c.keys())
print(d)

e = list(c.values())
print(e)

values = ChainMap()
values['x'] = 1

# add a new mapping

values = values.new_child()
values['x'] = 2

# add a new mapping

values = values.new_child()
values['x'] = 3

print(values)

#Discard  last mapping

values = values.parents
print(values['x'])

#Discard  last mapping
values = values.parents
print(values['x'])

#Using Merged Dict
a = {'x':1,'z':3}
b = {'y':2,'z':4}

merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

#Merged Dict with Chainmap

a = {'x':1,'z':3}
b = {'y':2,'z':4}


merger = ChainMap(a,b)
print(merged)
#print(merged['x'])
a['x'] = 42
v = merged['x']
print(v)