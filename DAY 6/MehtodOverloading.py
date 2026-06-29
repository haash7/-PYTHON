# method overloading:
# - function with same name insie the class

class demo:
   # def add(self,a):
    #    print(a)

   # def add(self,a,b):
    #    print(a+b)
    def add(self,*numbers):
        print(sum(numbers))


# MAIN 
obj = demo()
obj.add(8.9,7,6)
obj.add(10)
obj.add(10,20)           