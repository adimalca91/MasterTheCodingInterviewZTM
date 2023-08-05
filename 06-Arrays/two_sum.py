
'''
Leetcode Arrays - Two Sum problem
'''

'''
Approach 1: Brute Force

Time Complexity - O(n^2)
Space Complexity - O(1)
'''

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]
                    

'''
Approach 2: Two-pass Hash Table
We can reduce the lookup time from O(n) to O(1) by trading space for speed.

Time complexity - O(n).
We traverse the list containing n elements exactly twice.
Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n).

Space complexity - O(n).
The extra space required depends on the number of items stored in the hash table,
which stores exactly n elements.
'''

def two_sum_2(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    print(hash_map)
    for j in range(len(nums)):
        diff = target - nums[j]
        if diff in hash_map and hash_map[diff] != j:
            return [j, hash_map[diff]]
            

'''
Approach 3: One-pass Hash Table

Time complexity - O(n).
We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.

Space complexity - O(n).
The extra space required depends on the number of items stored in the hash table,
which stores at most n elements.
'''

def two_sum_3(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_map:
            return [i, hash_map[diff]] # Remember, in the first interation the dict is empty!
        hash_map[nums[i]] = i
        
        
print(two_sum([2,11,15,7,3], 9)) 
print(two_sum_2([2,11,15,7,3], 9))  
print(two_sum_3([2,11,15,7,3], 9))

