class Car:
    total_car_count = 0 

    def __init__(self, model, company):
        self.__model = model #encapsulation make mode private and cant be accessed outside the class with any instance
        self.company = company
        Car.total_car_count += 1
    
    @staticmethod
    def car_description(): #a method that belongs to class rather than instance of class
        return "car is basic means of transport"


    @property  #make method a property so for call we do not need to give get_model() but instead we can give get_model only
    def get_model(self): # now only accessed by method
        return f"{self.__model} !!!"

    def fullname(self):
        return f"{self.company} {self.__model}"

    def fuel_type(self):
        return "petrol"

class ElectricCar(Car):
    def __init__(self, model, company, battery_size):
        super().__init__(model, company)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electricity"

tesla_car = ElectricCar("X", "tesla", "90kwh")
tata_car = Car("punch", "tata")

# print(tesla_car.fullname())
# print(tesla_car.battery_size)

# print(tata_car.company)
# # print(tata_car.model) <-- this gives an error as model is private now encapsuled
# print(tata_car.get_model)
# # print(tata_car.fullname())

#### polymorphism
print(tata_car.fuel_type())
print(tesla_car.fuel_type())



### car count
print(tesla_car.total_car_count) #wrong practice as we need to have an instance to do that shit
print(Car.total_car_count)



##static method
# print(tata_car.car_description()) # required self,  and after static method gives error even with self that mean now method only assecciblke by class not instance
print(Car.car_description()) #doesnt required self 



##isinstance
class HybridCar:
    pass
print(isinstance(tesla_car, ElectricCar))
print(isinstance(tesla_car, Car))
print(isinstance(tesla_car, HybridCar))


class Battery:
    def battery_info(self):
        return"battery battery"
class Engine:
    def engine_info(self):
        return"enfine engine"
class NewElectric(Battery, Engine, Car):
    pass

nissan_car = NewElectric("gtr", "nissan")
print(nissan_car.battery_info())
print(nissan_car.engine_info())
