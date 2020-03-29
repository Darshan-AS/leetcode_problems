class Solution:
    ROMAN_DIGITS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    def intToRoman(self, num: int) -> str:
        
        roman_num, k = [], 0
        while num:
            x = num % 10
            num = num // 10
            roman_num.append(self.digit_to_roman(x, k))
            k += 2
        
        return ''.join(reversed(roman_num))
    
    def digit_to_roman(self, digit: int, index: int) -> str:
        if digit == 9:
            return self.ROMAN_DIGITS[index] + self.ROMAN_DIGITS[index + 2]
        elif digit == 4:
            return self.ROMAN_DIGITS[index] + self.ROMAN_DIGITS[index + 1]
        
        roman_digit = '' if digit < 5 else self.ROMAN_DIGITS[index + 1]
        return roman_digit + (self.ROMAN_DIGITS[index] * (digit % 5))
