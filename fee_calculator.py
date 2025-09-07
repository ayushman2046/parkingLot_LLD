
from datetime import datetime
import math


class FeeCalculator:
    fee_per_hour = {
        "Bike" : 10,
        "Car" : 20,
        "Truck": 30
    }

    @staticmethod
    def calculate_fee(ticket):
        if ticket.end_time is None:
            ticket.end_time = datetime.now()
        duration = ticket.end_time - ticket.start_time

        hours = math.ceil(duration.total_seconds() / 3600)
        rate = FeeCalculator.fee_per_hour(ticket.vehicle_type)

        return rate*hours