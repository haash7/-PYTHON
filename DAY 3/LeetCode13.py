InputRoman = input("Enter the Roman Value")
Romandict = {
'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000,
}
total = 0
for i in range (len(InputRoman)-1):
    if Romandict[InputRoman[i]]<Romandict[InputRoman[i+1]]:
        total = total-Romandict[InputRoman[i]]
    else:
        total = total+Romandict[InputRoman[i]]
total = total+Romandict[InputRoman[-1]]
print(total)            
