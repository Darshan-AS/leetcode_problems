class Solution:
    def countArrangement(self, n: int) -> int:
        def count_arrangement(index: int, used=None):
            if index > n: return 1
            used = used if used else set()
            count = 0
            for i in range(1, n + 1):
                if i not in used and (i % index == 0 or index % i == 0):
                    used.add(i)
                    count += count_arrangement(index + 1, used)
                    used.remove(i)
            return count
        
        return count_arrangement(1)
