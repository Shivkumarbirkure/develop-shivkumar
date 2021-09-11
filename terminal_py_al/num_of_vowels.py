#find the number of vowels present in the given string using sets



def find_no_vowels(s):

    vowels_count=0
    vowels_list=set('aeiou')
    for vowels in s:
        if vowels in vowels_list:
            vowels_count = vowels_count+1
    return vowels_count

s= "hello world how are you i am shivkumar Birkure"
print(find_no_vowels(s))

