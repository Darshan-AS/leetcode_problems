class Solution:
    def average(self, salary: list[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
