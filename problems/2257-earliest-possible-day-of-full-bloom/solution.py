class Solution:
    def earliestFullBloom(self, plant_time: list[int], grow_time: list[int]) -> int:
        return reduce(
            lambda a, x: (max(a[0], a[1] + x[1] + x[0]), a[1] + x[1]),
            sorted(zip(grow_time, plant_time), reverse=True),
            (0, 0),
        )[0]
