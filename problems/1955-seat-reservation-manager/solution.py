class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n + 1))
        heapify(self.seats)

    def reserve(self) -> int:
        return heappop(self.seats)

    def unreserve(self, seat_number: int) -> None:
        heappush(self.seats, seat_number)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
