

# We are going to design parking Lot at low level
** Functional requirements **
``` 
1. A parking lot has masny floors
2. each floor contains maqny vehicles of different types
3. when A vehicke arrives book a slot for it and issue a ticket also
4. when A vehicle leaves free that slot and calculate the fee.
```

** Non functional requirements**
```
1. System should be scalable to handle multiple vehicles and flexible enough for future to handle more different type of vehicles
2. Low latency for all the operations including booking and freeing the space.
```

```
Entities: 
    - Parking Lot
    1. Parking Slot
    2. Vehicle
    3. parking floor
    4. ticket
```

```
class relationships : 
    - parking lot -> parking floor -> parking slot -> vehile -> ticket
```

```
Define Classes: 
    1. ParkingLot : 
        a. name
        b. floor
        c. park_vehicle()
        d. unpark_vehicle()
    2. ParkingFloor:
        a. floor_number
        b. slot
    3. ParkingSlot:
        a. Occupied - True/False
        b. slot_id
        c. slot_type (for vehicle)
        d. park_vehicle()
        e. unpark_vehicle()
    4. Vehicle: 
        a. liscense_plate
        b. Color
        c. vehicle_type
    5. Ticket
        a. ticket_id
        b. slot_id
        c. vehicle_time
        d. entry_time
        e. end_time
    