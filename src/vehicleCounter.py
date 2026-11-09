class VehicleCounter:
    def __init__(self):
        self.counter = 0
        self.countedVehc = set()

    def update(self, trackId):
        if trackId is None:
            return

        if trackId not in self.countedVehc:
            self.countedVehc.add(trackId)
            self.counter += 1
            print(f"New vehicle: {trackId}, Total: {self.counter}")




