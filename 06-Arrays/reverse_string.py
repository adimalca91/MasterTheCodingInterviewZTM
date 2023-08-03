'''
Reverse a string
'''

def reverse(str):
    reverse_lst = []
    
    for i in range(len(str)-1, 0, -1):
        reverse_lst.append(str[i])
    
    reverse_str = ''.join(reverse_lst)
    return reverse_str

        