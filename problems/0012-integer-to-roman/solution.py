class Solution:
    roman_digits = { 
        1000: 'M', 
        900: 'CM', 
        500: 'D', 
        400: 'CD', 
        100:'C', 
        90:'XC', 
        50:'L', 
        40:'XL', 
        10: 'X', 
        9: 'IX', 
        5:'V', 
        4: 'IV', 
        1: 'I',
    }
    
    def intToRoman(self, num: int) -> str:
        roman_num, k = [], 0
        for k, v in self.roman_digits.items():
            if num // k:
                x, num = divmod(num, k)
                roman_num.append(v * x)
        
        return ''.join(roman_num)
    
