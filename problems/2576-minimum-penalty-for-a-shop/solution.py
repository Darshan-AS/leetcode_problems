class Solution:
    def bestClosingTime(self, customers: str) -> int:
        return min(zip(accumulate(map({'Y': -1, 'N': 1}.get, customers), initial=0), count()))[-1]

