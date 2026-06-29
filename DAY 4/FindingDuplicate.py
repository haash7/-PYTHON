L = list(map(int,input("enter the number :").split()))
s = set(L)
a = len(L)
b = len(s)
if a==b:
    print(False)
else:
    print(True)
