from hashlib import new
from itertools import count

arr1 = [1,1,6,7,8,7,8,2,3]

newarr = []
def singelnumber(nums):
    arr1.sort()
    for i in nums :
        counter = 0
        for k in nums:
            if i == k :
                counter += 1 
        
        if counter == 1:
            newarr.append(i)
        
    
    print(newarr)
                

singelnumber(arr1)
