class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        sum, carry = 0, 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >=0:
            temp = carry
            
            if i >= 0:
                temp += int(a[i])
                i -= 1
            
            if j >= 0:
                temp += int(b[j])
                j -= 1
                
            sum = temp % 2
            carry = temp // 2
            result.append(str(sum))
        
        if carry:
            result.append('1')
        
        return ''.join(result[::-1]) if result else '0'
