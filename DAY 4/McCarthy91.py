def mccarthy(n):
    if n>100:
        return n-10
    return mccarthy(mccarthy(n+11))
# driver code
n = int(input("enter the number :"))
print("number : ",mccarthy(n))