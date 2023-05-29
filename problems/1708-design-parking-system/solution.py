class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, car_type: int) -> bool:
        self.slots[car_type] = s = max(self.slots[car_type] - 1, -1)
        return s > -1


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
