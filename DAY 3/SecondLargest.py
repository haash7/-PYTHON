a = int(input(" enter the number for a :"))
b = int(input(" enter the number for b :"))
c = int(input(" enter the number for c :"))
if (a > b and a < c) or ( a < b and a > c) :
    print (" a is the second largest number ");
elif (b > a and b < c) or (b < a and b> c):
    print ( " b is the second largest number ");
else:
    print( " c is the second largest ");