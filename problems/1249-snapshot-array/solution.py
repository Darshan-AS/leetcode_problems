class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history = [[[self.id, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        h = self.history[index]
        if  self.id > h[-1][0]: h.append([self.id, val])
        else: h[-1][1] = val

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect_right(self.history[index], snap_id, key=itemgetter(0))
        return self.history[index][snap_index - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
