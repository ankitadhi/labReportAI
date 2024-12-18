class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    def start(self):
        print("Starting engine")
    def stop(self):
        print("Stopping engine")

class Wheel:
    def __init__(self, wheel_type):
        self.wheel_type = wheel_type

class Car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel

    def start_car(self):
        self.engine.start()
        print("Car Started")
engine = Engine('auto')
wheel = Wheel('pauto')

car = Car(engine, wheel)
car.start_car();
        