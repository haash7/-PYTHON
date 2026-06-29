nums = {3,2,4}
target = 6
d = {}
for i , num in enumerate(nums):
    complement = target - num

    if complement in d :
        print(d[complement],"  ",i)
        d[num]=i