#multiply all the items in the dict.
def ml(n):
    multi=1
    for i in n.values():
        multi=multi*i
        i+=1
    return multi

n={'A':2,'B':3,'C':4,'d':6}
print(ml(n))