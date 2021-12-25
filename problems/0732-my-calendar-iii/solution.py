from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.__events_count = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.__events_count[start] = self.__events_count.get(start, 0) + 1
        self.__events_count[end] = self.__events_count.get(end, 0) - 1
                
        return max(accumulate(self.__events_count.values()))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
