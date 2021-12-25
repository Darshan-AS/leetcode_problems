from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.__events = SortedList()

    def book(self, start: int, end: int) -> bool:
        event = (start, end)
        i = self.__events.bisect_left(event)

        n = len(self.__events)
        if (i < n and self.__overlaps(event, self.__events[i])) or (
            i > 0 and self.__overlaps(event, self.__events[i - 1])
        ):
            return False

        self.__events.add(event)
        return True

    def __overlaps(self, e1: tuple[int, int], e2: tuple[int, int]) -> bool:
        start, end = max(e1[0], e2[0]), min(e1[1], e2[1])
        return start < end


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
