i = 5
print(i)
i = i+1
print(i)

for i in range(5):
    for j in range(i,5):
        j = j+1 
        print(j,end='')
    print('')

for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")