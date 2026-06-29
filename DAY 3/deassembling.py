name = str("pintu")
l = len(name)
mid = len(name)//2
# name[start:end]
firstpart = name[0:mid]
secondpart = name[mid:]
# reverse
firstpart = name[:mid]
revfirstpart = firstpart[::-1]
revsecondpart = secondpart[::-1]
result = revfirstpart+revsecondpart
print(result)


