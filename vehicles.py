from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    BIKE = "Bike"
    CAR = "Car"
    TRUCK = "Truck"

class Vehicle(ABC):
    def __init__(self, liscense_plate, vehicle_type):
        self.liscense_plate = liscense_plate
        self.vehicle_type = vehicle_type


class Bike(Vehicle):
    def __init__(self, liscense_plate):
        super().__init__(liscense_plate, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self, liscense_plate):
        super().__init__(liscense_plate, VehicleType.CAR)

class Truck(Vehicle):
    def __init__(self, liscense_plate):
        super().__init__(liscense_plate, VehicleType.TRUCK)