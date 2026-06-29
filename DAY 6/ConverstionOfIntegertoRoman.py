class intToromanConverter:
    def int_to_roman(self,num):
        romanValues=["M","CM","D","CD","XC","L","XL","X","IX","V","IV","I"]
        integer=[1000,900,500,400,100,90,50,40,9,5,4,1]
        romanEqual=""

        for i in range(len(integer)):
            while num>=integer[i]:
                romanEqual+=romanValues[i]
                num-=integer[i]

        return romanEqual


#INPUT
num=int(input("enter the number:"))
obj=intToromanConverter()
print(obj.int_to_roman(num))        
