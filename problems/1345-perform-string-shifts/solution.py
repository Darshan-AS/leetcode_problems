class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        resultant_shifts = 0
        for direction, magnitude in shift:
            resultant_shifts += magnitude if direction == 0 else -magnitude
            resultant_shifts %= len(s)
        
        return s[resultant_shifts:] + s[:resultant_shifts]
        
