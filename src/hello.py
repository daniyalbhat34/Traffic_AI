from vehicleCounter import VehicleCounter

counter = VehicleCounter(430)

counter.update(12, 450)
counter.update(12, 440)
counter.update(12, 425)

print(counter.counter)