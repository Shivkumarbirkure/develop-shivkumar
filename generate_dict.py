#generate a dictonary that contains number between 1 to n in form of x:x*x

def num(n):
    d={x:x*x for x in range(1,n+1)}
    print(d)
n=5
(num(n))

