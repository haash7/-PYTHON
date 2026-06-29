def addtwostring(num1,num2):
    i = len(num1)-1
    j = len(num2)-1


    carry = 0
    result = []

    while i>=0 or j>=0 or carry:
        digit1=ord(num1[i]-ord('0')) if i>=0 else 0 
        digit2=ord(num2[j]-ord('0'))  if j>=0 else 0

        total=digit1+digit2+carry
        result.append(str(total%10))
        caart=total//10

        i-=1
        j-=1
        return ''.join(result[::-1])
    
# main
num1=input("enter the first value :") 
num2=input("enter the second value : ")
print(addtwostring(num1,num2))   
