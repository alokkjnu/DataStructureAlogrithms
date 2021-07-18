#Mapping Names to sequence element

from collections import namedtuple

subscriber = namedtuple('subscriber',['addr','joined'])
sub = subscriber('alok@gmail.com','2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr,joined = sub
print(addr)
print(joined)

def compute_cost(records):
    total = 0.0
    for rec in records:
        total +=rec[1]*rec[2]
    return total
print(compute_cost)


stock = namedtuple('stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total += s.shares * s.price
    return total

s = stock('ACME',100,123.45)
print(s)
#s.shares = 75

s = s._replace(shares =75)
print(s)

stock = namedtuple('stock',['name','shares','price','date','time'])
stock_prototype = stock('',0,0.0,None,None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME','shares':100,'price':123.45}
print(dict_to_stock(a))
b = {'name' : 'ACME','shares': 100, 'price' : 123.45, 'date':'12/17/2021', 'time' : None}
print(b)
