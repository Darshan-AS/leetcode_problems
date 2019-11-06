class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        pair_map = {}
        
        for index, value in enumerate(numbers):
            required_pair = target - value
            if required_pair in pair_map.keys():
                return [pair_map[required_pair] + 1, index + 1]
            
            pair_map[value] = index
