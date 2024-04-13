'''
Merge sorted arrays
'''

def merge_sorted_arrays(arr1, arr2):
    
    '''
    Using this function we are running over the lists with a direct access operation.
    We dont use here another pointer to point to each item in the list.
    '''
    
    if arr1 == []:
        return arr2
    elif arr2 == []:
        return arr1
    
    merged_arr = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i+=1

        else:
            merged_arr.append(arr2[j])
            j+=1
    
    merged_arr += arr1[i:] + arr2[j:]
    return merged_arr



def merge_sorted_arrays_2(arr1, arr2):
    
    '''
    Using this function we are actually running over the lists with a pointer on each list.
    Once one of these pointers reaches the end of it's list (None) we know to stop and
    then merge the entire other list to the merged one.
    '''
    if arr1 == []:
        return arr2
    elif arr2 == []:
        return arr1
    
    merged_arr = []
    i = 0
    j = 0
    cur1 = arr1[i]
    cur2 = arr2[j]
    
    while (cur1 != None and cur2 != None):
        if cur1 <= cur2:
            merged_arr.append(cur1)
            i+=1
            if(i<len(arr1)):
                cur1 = arr1[i] # the increment of the while loop
            else:
                cur1 = None    # a sign to stop the loop
            
        else:
            merged_arr.append(cur2)
            j+=1
            if(j<len(arr2)):
                cur2 = arr2[j] # the increment of the while loop
            else:
                cur2 = None    # a sign to stop the loop
    
    if cur1 == None:
        merged_arr += arr2[j:]
    else:
        merged_arr += arr1[i:]
    
    
    return merged_arr          


# a=[1,3,4,6,20]
# b=[2,3,4,5,6,9,11,76, 77, 80, 82, 84, 200, 204]
# c=[0,3,4,31]
# d = [4,6,30]
# print(merge_sorted_arrays_2(a,c))

'''
    Note: I increment i as such i+=1 and only after that I assign cur1 = arr1[i] and therefore if i
    is greater than the length of the list (after the incrementation) i will get index out
    of range error and the function will stop and exit. So, to solve this issue I have a check condition
    after the incrementation, but before the assignment so that if its greater then len(arr) then we assign
    this pointer cur None, and thats a sign that we have reached the and of this list and we have iterated
    on all it's items and merged them.
    
    This was not an issue in the first function above since we did not have other pointers to the lists
    and therefore we only had an incrementation then the while loop checked its conditions. So, we did not
    have an assignment right after the incrementation, only after the loop was checked!
'''

'''
Another implementation using a for loop
'''

def add_rest(merged_arr, arr, index):
    for i in range(index, len(arr)):
        merged_arr.append(arr[i])
    return merged_arr
        

def merge_sorted_arrays_3(arr1, arr2):
    x = 0
    y = 0
    temp1 = arr1[x]
    temp2 = arr2[y]
    arr = []
    
    for i in range(len(arr1)+len(arr2)):
        if temp1 < temp2:
            arr.append(temp1)
            if x < len(arr1)-1:
                x+=1
                temp1 = arr1[x]
            else:
                return add_rest(arr ,arr2, x+1)
        elif temp1 > temp2:
            arr.append(temp2)
            if y < len(arr2)-1:
                y+=1
                temp2 = arr2[y]
            else:
                return add_rest(arr, arr1, y+1)
        else:
            arr.append(temp1)
            arr.append(temp2)
            if x < len(arr1)-1:
                x+=1
                temp1 = arr1[x]
            else:
                return add_rest(arr ,arr2, x+1)
            if y < len(arr2)-1:
                y+=1
                temp2 = arr2[y]
            else:
                return add_rest(arr, arr1, y+1)
    
    
# c=[0,3,4,5, 17,31]
# d = [1,2,4,6,30]
# print(merge_sorted_arrays_3(c,d))
