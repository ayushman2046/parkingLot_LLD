from datetime import datetime
import uuid
class Ticket:
    def __init__(self, slot_id, vehicle_type):
        self.slot_id = slot_id
        self.vehicle_type = vehicle_type
        self.ticket_id = str(uuid.uuid1())
        self.start_time = datetime.now()
        self.end_time = None
        self.fee = None
    
    def close_ticket(self, fee):
        self.end_time = datetime.now()
        self.fee = fee
    
    def __str__(self):
        return (f"Ticket[{self.ticket_id}] - Vehicle: {self.vehicle_type}, "f"Slot: {self.slot_id}, Entry: {self.entry_time}, Exit: {self.exit_time}, Fee: {self.fee}")