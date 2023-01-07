class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        return reduce(
            lambda a, x: (a[0], a1) if (a1 := a[1] + x[1]) >= 0 else (x[0] + 1, 0),
            enumerate(map(sub, gas, cost)),
            (0, 0), # (start_index, total_cost)
        )[0] if sum(gas) >= sum(cost) else -1
