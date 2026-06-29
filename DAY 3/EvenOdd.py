n = list(map(int,input(" enter the values").split()))
even = 0
odd = 0
for n in n:
    if n%2==0:
        even+=1
    else:
        odd+=1
print("odd : ", odd)
print("even :",even)           