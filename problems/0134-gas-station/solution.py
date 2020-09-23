class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = fuel = 0
        for i in range(2 * n):
            if start == i - n: return start
            fuel += gas[i % n] - cost[i % n]
            if fuel < 0:
                start = i + 1
                fuel = 0
        return -1
