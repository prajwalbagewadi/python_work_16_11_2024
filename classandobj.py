class Car:
    brand=""
    model=""
    price=0.00
    color=""
    def __init__(self,b,m,p,c):
        self.brand=b
        self.model=m
        self.price=p
        self.color=c
    def print(self):
        print("brand", self.brand)
        print("model",self.model)
        print("color", self.color)
        print("price", self.price)

car1=Car("Jeep","Compass",18.99,"Exotica Red")
car1.print()
car2=Car("BMW","M4",1.53,"Portimao Blue Metallic")
car2.print()
print(car2.brand



      )