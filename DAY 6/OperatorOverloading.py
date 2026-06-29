print(10+20)
print("hello"+"python")
print(5*4)
print("hi"*4)
# custom operator overloading

class book:
    def __init__(self,pages):
        self.pages=pages

    # magic method
    def __add__(self,others):
        return self.pages+others.pages

b1= book(200)
b2= book(300)
print(b1+b2)        