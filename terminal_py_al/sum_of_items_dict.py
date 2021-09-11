#sum of all items in the dictonary.
def sum_all(s):
    value_count=0
    for i in s.values():
        value_count=value_count+i
        i+=1
    return value_count
s={'A':100,'B':540,'C':239,'d':999}
print(sum_all(s))

