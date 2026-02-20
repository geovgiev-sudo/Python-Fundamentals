class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year


    def start_engine(self):
        print(f"The {self.make} {self.model} engine is starting.")

    def stop_engine(self):
        print(f"The {self.make} {self.model} engine is stopping.")


car1 = Car("Mercedes", "S500", 2022)
car2 = Car("BMW", "750", 2021)
car3 = Car("Toyota", "Supra", 2018)

print(car1.make)
print(car2.make)
print(car3.make)
car1.start_engine()
car2.start_engine()
car3.start_engine()
car1.stop_engine()
car2.stop_engine()
car3.stop_engine()