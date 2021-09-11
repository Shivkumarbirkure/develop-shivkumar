#check comman letters in two input strings.

def input_strings(let1,let2):
    comman=0
    for i in let1:
        if i in let2:
            comman=comman+1

    return comman


let1="abcdef"
let2="cb"
print(input_strings(let1,let2))
