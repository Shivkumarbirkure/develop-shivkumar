
#map two lists into a dictonary
key = []
value = []
n = int(input("enter n :"))
for i in range(n):
    element=int(input("enter number to append in list:"))
    key.append(element)

for i in range(n):
    elements1=int(input("enter:" ))
    value.append(elements1)


d= dict(zip(key,value))
print(d)