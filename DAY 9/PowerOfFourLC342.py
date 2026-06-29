def PowerOfFour(self , n):
    n = 0
    if n<=0:
        return False
    
    while n%4==0:
        n=n//4

    return n==1

#MAIN 
n = 16
print(PowerOfFour(n))    