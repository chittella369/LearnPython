from Abstract import Car
from Abstract import Truck
from Abstract import SportsCar


cars = [Truck('Bananatruck'), Truck('Orangetruck'), SportsCar('Z3')]

for car in cars:
    print(car.name + ":" + car.drive())
