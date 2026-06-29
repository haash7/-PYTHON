n = eval(input("enter the input"))
k = int(input("enter the column index k :"))
product = 1
for tup in n :
    product=product*tup[k]
print(f"product of values : {k}): {product}")