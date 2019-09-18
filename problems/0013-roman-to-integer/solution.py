class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        prev = 0
        num = 0
        for i in s[::-1]:
            value = roman_to_int_map[i]
            num += value if value >= prev else -value
            prev = value
        
        return num
