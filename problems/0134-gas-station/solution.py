class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = fuel = i = count = -1
        b = 0
        while (i := (i + 1) % n) != start and (count := count + 1) <= 2 * n:
            if fuel < b:
                fuel = b = 0
                start = i
            fuel += gas[i] - b
            b = cost[i]
        
        return start if fuel - b >= 0 and count <= 2 * n else -1
        
