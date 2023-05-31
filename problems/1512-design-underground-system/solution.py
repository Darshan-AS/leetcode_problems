class UndergroundSystem:

    def __init__(self):
        self.check_ins = {} # station_in => t_in
        self.trips = defaultdict(lambda: (0, 0)) # (station_in, station_out) => (total_t, count) across all trips

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        self.check_ins[id] = (station_name, t)

    def checkOut(self, id: int, station_name: str, t: int) -> None:
        s_out, t_out = station_name, t
        s_in , t_in  = self.check_ins[id]

        self.trips[(s_in, s_out)] = tuple(map(add, self.trips[(s_in, s_out)], (t_out - t_in, 1)))

    def getAverageTime(self, station_in: str, station_out: str) -> float:
        return truediv(*self.trips[(station_in, station_out)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
