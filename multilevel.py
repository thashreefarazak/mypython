class Calculation:
    def add(self,a,b):
        return a+b
class Calculation2:
    def sub(self,a,b):
        return a-b
class Calculation3:
    def div(self,a,b):
        return a/b
class Calculation4(Calculation,Calculation2,Calculation3):
    def mul(self,a,b):
        return a*b
d=Calculation4()
print(d.add(2,3))
print(d.sub(4,2))
print(d.div(10,2))
print(d.mul(2,3))
