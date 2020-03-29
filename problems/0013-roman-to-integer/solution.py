class Solution:
    roman_to_digits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        int_s, i = 0, 0
        while i < len(s):
            if i + 1 < len(s) and self.roman_to_digits[s[i + 1]] > self.roman_to_digits[s[i]]:
                int_s += self.roman_to_digits[s[i + 1]] - self.roman_to_digits[s[i]]
                i += 2
            else:
                int_s += self.roman_to_digits[s[i]]
                i += 1
        
        return int_s
