from itertools import zip_longest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add_ch(x, y, c):
            ord_0 = ord('0')
            # total = (ord(x) - ord_0) + (ord(y) - ord_0) + (ord(c) - ord_0)
            total = ord(x) + ord(y) + ord(c) - 3 * ord_0
            sum_, carry = total % 10, total // 10
            return chr(ord_0 + sum_), chr(ord_0 + carry)
            
        
        def iter_add(num1_s, num2_s):
            carry = '0'
            for ch1, ch2 in zip_longest(reversed(num1_s), reversed(num2_s), fillvalue='0'):
                sum_, carry = add_ch(ch1, ch2, carry)
                yield sum_
            
            if carry != '0':
                yield carry
        
        return ''.join(reversed(tuple(iter_add(num1, num2))))
