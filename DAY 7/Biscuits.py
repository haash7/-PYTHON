# leetcode1011
def shippingcapacity(weight,days):
    weight = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    left = max(weight)
    right = sum(weight)


    while left<=right:
        mid = left + (right-left)//2
        total_days = 1
        current_load = 0
        answer = right

        for w in weight:
           if current_load+w>mid:
               total_days+=1
               current_load=0
           current_load+=w    
    
        if total_days<=days:
            answer = mid
            right = mid-1

        else:
            left =  mid+1

    return answer   

    print(answer)

# driver code
weight = [1,2,3,4,5,6,7,8,9,10]
days=5
print(shippingcapacity(weight,days))






