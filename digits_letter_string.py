#count the number of digits and letters in the string 

def digits_letters(s):
    count_num=0
    count_char=0
    for i in s:
        if i.isnumeric():
            count_num=count_num+1
        else:
            count_char=count_char+1
    print("characters count:",count_char)
    print("number count:",count_num)
s= "12sjije2y33"
digits_letters(s)
