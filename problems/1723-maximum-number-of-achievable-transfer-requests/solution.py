class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        def max_requests(i: int, emp_deltas: list[int]) -> int:
            if i >= len(requests): return -inf if any(emp_deltas) else 0
            u, v = requests[i]

            skip = max_requests(i + 1, emp_deltas)

            emp_deltas[u] -= 1; emp_deltas[v] += 1
            take = max_requests(i + 1, emp_deltas)
            emp_deltas[u] += 1; emp_deltas[v] -= 1

            return max(skip, take + 1)
        
        return max_requests(0, [0] * n)
