class Vehicle:
    def __init__(self,name,maxspeed,mileage,engine):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.engine=engine

class Bus(Vehicle):
    pass

b2=Bus("School Volvo",123,67,"V8")
print("Name of school bus is {} with max speed of {} and mileage of {}mph with a engine{}".format(b2.name,b2.maxspeed,b2.mileage,b2.engine))
b3=Bus("School Leyland",123,65,"ZD30 DDTi")
print("Name of school bus is {} with max speed of {} and mileage of {}mph with a engine{}".format(b3.name,b3.maxspeed,b3.mileage,b3.engine))