#Determining the most Frequently Occuring Items in a Sequence
from collections import Counter

words = [ 
    'look', 'into', 'my', 'eyes','look', 'into', 'my', 'eyes','the','eyes','the','eyes','the',
    'eyes','not','around','the','eyes',"don't",'look','around','the','eyes','look', 'into', 'my', 'eyes',
    "you're",'under','my','eyes']

word_count = Counter(words)
top_three = word_count.most_common(3)
print(top_three)
print(word_count['eyes'])
print(word_count['not'])

#Increment the count manually

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_count[word] +=1
print(word_count['eyes'])

#combining Dictionaries using mathematical operators
#combine Counts
a = Counter(words)
print(a)
b = Counter(morewords)
print(b)
c = a+b
print(c)

#subtract Countss
a = Counter(words)
print(a)
b = Counter(morewords)
print(b)
c = a-b
print(c)