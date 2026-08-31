nums=[1,2,3,4,5,2,1]

duplicates=[]




for num in nums :
    if num not in duplicates and nums.count(num) > 1:
        duplicates.append(num)  

print(duplicates)