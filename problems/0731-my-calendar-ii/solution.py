from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.__events_count = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.__events_count[start] = self.__events_count.get(start, 0) + 1
        self.__events_count[end] = self.__events_count.get(end, 0) - 1
                
        if 3 in accumulate(self.__events_count.values()):
            self.__events_count[start] -= 1
            self.__events_count[end] += 1
            return False
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
