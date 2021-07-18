#Unpacking Element from Iterable of Arbitrary

#def drop_first_last(grades):
#    first, *middle, last = grades
#    return avg(middle)

record = ("Dave","dave@gmail.com","8696617717","9721189988")
name, email, *phone_number = record
print("name : ", name)
print("email : " ,email)
print("phone nu : ",phone_number)

*trailing, current= [10,8,7,1,9,5,10,3]
print("triling : ",trailing)
print("current : ", current)

record = ('ACME',50,125.42,(12,18,2012))
name,*_,(*_,year)= record
print("name : ",name)
print("year : ",year)

item = [1,10,7,8,6,3,4]
head,*trail = item
print("head : ",head)
print("trail : ",trail)

def sum(item):
    head,*trail = item
    return head + sum(trail) if trail else head
print(sum(item))