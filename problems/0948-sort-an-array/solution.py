class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quicksort(seq):
            if len(seq) <= 1: return seq

            pivot = random.choice(seq)
            lt = [v for v in seq if v < pivot]
            eq = [v for v in seq if v == pivot]
            gt = [v for v in seq if v > pivot]

            return quicksort(lt) + eq + quicksort(gt)
        
        return quicksort(nums)
