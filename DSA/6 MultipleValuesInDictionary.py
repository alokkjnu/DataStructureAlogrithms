#Mapping Key to multiple Value in a Dictionary

d = {
    'a' : [1,2,3],
    'b' : [4,5]
}
e = {
    'a' : [1,2,3],
    'b' : [4,5]
}
print(d['a'])

a = {'alok':1,'uday':2}
print(a['alok'])

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(4)

d = defaultdict(set)
print(d)

d['a'].add(1)
d['b'].add(2)
d['c'].add(4)
print(d)

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('b',[]).append(2)
d.setdefault('c',[]).append(4)
print(d)

d = {}
for key,value in d:
    if key not in d:
        d[key]=[]
    d[key].append(value)

d = defaultdict(list)
for key, value in d:
    d[key].append(d)