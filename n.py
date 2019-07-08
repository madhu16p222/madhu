character = 256
def max(str, n):
    count = [0] * character
    for i in range(n):
        count[ord(str[i])] += 1
    max_distinct = 0
    for i in range(character):
        if (count[i] != 0):
            max_distinct += 1	
    return max_distinct 

def Substr(str):
    n = len(str)	
    max_distinct = max(str, n) 
    num = n	 
    for i in range(n):
        for j in range(n):
            subs = str[i:j]
            su_l = len(subs) 
            su_char = max(subs, su_l)
            if (su_l < num and max_distinct == su_char):
                num = su_l
    return num

string=input()
result=Substr(string)
print(result)

