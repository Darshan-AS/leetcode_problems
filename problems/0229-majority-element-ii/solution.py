class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = [None, None]
        counts = [0, 0]
        
        for i in nums:                
            if i == candidates[0] or (counts[0] == 0 and i != candidates[1]):
                candidates[0] = i
                counts[0] += 1
            elif i == candidates[1] or (counts[1] == 0 and i != candidates[0]):
                candidates[1] = i
                counts[1] += 1
            else:
                counts[0] -= 1
                counts[1] -= 1
        
        counter = {candidates[0]: 0, candidates[1]: 0}
        for i in nums:
            if i == candidates[0]: counter[candidates[0]] += 1
            elif i == candidates[1]: counter[candidates[1]] += 1
        
        return [k for k, v in counter.items() if v > len(nums) // 3]
