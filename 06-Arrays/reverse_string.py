'''
Reverse a string
'''

def reverse(str):
    reverse_lst = []
    
    for i in range(len(str)-1, -1, -1):
        reverse_lst.append(str[i])
    
    reverse_str = ''.join(reverse_lst)
    return reverse_str


def reverse_str(str):
    len_str = len(str)
    reversed = ""
    for i in range(len_str-1,-1,-1):
        reversed += str[i]
    return reversed


print(reverse("hello this is me"))
print()
print(reverse_str("hello this is me"))