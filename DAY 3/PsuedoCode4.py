n = int(input("enter the number"))
n = n*n
num=len(str(n))
first= n%(10**num)
second= n//(10**num)
if first+second==n:
    print("kreprekar number ")
else:
    print("not kreprekar number")    






