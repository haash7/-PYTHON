num = input("enter the number :")
increasing = True 
Decreasing = True
for i in range (len(num)-1):
    if int(num[i+1])!=int(num[i])+1:
        increasing = False;
    if int(num[i+1])!=int(num[i])-1:
        decreasing = True;
if increasing:
    print(" Increasing Fancy Number ");
elif decreasing:
    print(" Decreasing Fancy NUmber  ");
else:
    print(" Not a Fancy Number ");



