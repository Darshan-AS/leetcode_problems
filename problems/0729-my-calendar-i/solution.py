class MyCalendar:

    def __init__(self):
        self.__events = []

    def book(self, start: int, end: int) -> bool:
        event = (start, end)
        overlaps_with_event = partial(self.__overlaps, event)
        
        if any(map(overlaps_with_event, self.__events)): return False
        
        self.__events.append(event)
        return True

    def __overlaps(self, e1: tuple[int, int], e2: tuple[int, int]) -> bool:
        start, end = max(e1[0], e2[0]), min(e1[1], e2[1])
        return start < end


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
