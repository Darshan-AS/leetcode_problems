class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        garbage_sets  = map(set, reversed(garbage))
        truck_visits  = map(len, accumulate(garbage_sets, or_))
        travel_times  = map(mul, truck_visits, reversed(travel))
        garbage_times = map(len, garbage)
        return sum(travel_times) + sum(garbage_times)

