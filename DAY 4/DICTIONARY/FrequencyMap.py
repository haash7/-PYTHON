n = list(map(int,input("enter the number")))
k = int(input("enter the threshold value k :"))
freq = dict()

for num in n:
    freq[num]=freq.get(num,0)+1
for num,count in freq.item():
    if count > k:
        print(f"{num}:{count} times")
