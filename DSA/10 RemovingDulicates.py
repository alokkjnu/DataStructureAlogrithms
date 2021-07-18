#Removing duplicates from a sequence while maintaining order
#Removing Duplicates from Sequence while Maintaining Order

from typing import ItemsView


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [0,1,2,3,1,3,1,4,1,5,6,1,4,2,2,3,5,34,5,6,4,3,7,7,54]
b = list(dedupe(a))
print(b)

def dedupe(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield seen
            seen.add(val)

a = [{'x': 1, 'y': 2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
b = list(dedupe(a, key= lambda d:(d['x'],d['y'])))
print(b)
c = list(dedupe(a,key=lambda d:(d['x'])))
print(c)
