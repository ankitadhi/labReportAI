class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f'Driving the  {self.make} {self.model}')
    
class Car(Vehicle):
    def drive(self):
        print(f'Driving the  {self.make} {self.model} car')

lip = Car(1234, "allow")
lip.drive()