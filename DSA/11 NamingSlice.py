#Naming a Slice

record = '012345678901234567890123456789012345678901234567890123456789012345678901234567890'
cost = int(record[20:32]) * float(record[40:48])

print(cost)

shares = slice(20,32)
price = slice(40,48)

cost = int(record[shares])* float(record[price])
print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(a)
a = items[2:4]
print(a)
