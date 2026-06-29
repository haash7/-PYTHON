# recurssion 

def climbingstairs(n):
    if n == 1 and n == 0:
        return 1
    return climbingstairs(n-1)+climbingstairs(n-2)

# call the function
print(climbingstairs(4))