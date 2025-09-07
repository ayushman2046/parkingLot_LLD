
from enum import Enum
from vehicles import Vehicle


class SlotType(Enum):
    BIKE = "Bike"
    CAR = "Car"
    TRUCK = "Truck"


class ParkingSlot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.occupied = False
        self.vehicle = None
    
    def park_vehicle(self, vehicle):
        if self.occupied:
            raise Exception('Slot already covered')
        if self.slot_type != vehicle.vehicle_type:
            raise Exception(
                f"Slot {self.slot_id} is only for {self.slot_type} vehicles!"
            )
        self.occupied = True
        self.vehicle = vehicle
    
    def unpark_vehicle(self):
        if not self.occupied:
            raise Exception("No vehicle in the slot, might got stolen")
        self.occupied = False
        self.vehicle = None

        return self.vehicle
