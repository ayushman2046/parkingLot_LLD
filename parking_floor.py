
class ParkingFloor:
    def __init__(self, floor_num, slots):
        self.floor_num = floor_num
        self.slots = slots #----------- slots will be store as dictionary with key as some slot_id and then value as parking_slot
    
    def available_slot(self, vehicle_type):
        for slot in self.slots.values():
            if slot.slot_type == vehicle_type and slot.occupied == False:
                return slot
        return None
    
    def park_vehicle(self, vehicle):
        slot = self.available_slot(vehicle.vehicle_type)
        if not slot:
            raise Exception("No available slot, please try again later")

        slot.park_vehicle(vehicle)
        return slot

    def unpark_vehicle(self,slot_id):
        if slot_id not in self.slots:
            raise Exception("Slot id doesn't xist")
        
        slot = self.slots[slot_id]
        return slot.unpark_vehicle()
    
    def display_status(self):
        for slot in self.slots:
            if slot.occupied == True:
                print(f'{slot.slot_id} is occupied')
            else:
                print(f'{slot.slot_id} is free')
    

