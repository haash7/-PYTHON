# Two Pointer 
#1.Left
#2.right
def movezeroes(nums):
    left=0

    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            # a,b=b,a
            left=left+1

