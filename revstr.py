#Write a program reverse a given input string
"""
def reverse(str):
    y=""
    for i in range(len(str)-1, -1, -1):
        y=y+str[i]
        print(y)        
    return y
input_str1=raw_input("Enter a string:")
print reverse(input_str1)
"""

"""
def string_reverse(str1):
    rev_str = " "
    index = len(str1) 
    while(index>0):
        rev_str = rev_str + str1[index-1]
        index = index-1
    return(rev_str)

print(string_reverse('1tniop'))
"""
"""
def reverse(str):
    rev=""
    index=len(str)
    while(index>0):
        rev=rev+str[index-1]
        index=index-1
    return rev
print(reverse("sainadh"))
"""
