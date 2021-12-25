class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator != 0 and (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)
        
        q_left_int, r = divmod(n, d)
        
        seen = {}
        q_right_list = []
        index = 0
        while r != 0 and r not in seen:
            seen[r] = index
            q, r = divmod(r * 10, d)
            q_right_list.append(str(q))
            index += 1
        
        q_left = str(q_left_int)
        q_right = ''.join(q_right_list)
        
        if not r: return f"{sign}{q_left}{'.' if q_right else ''}{q_right}"
        
        i = seen[r]
        return f'{sign}{q_left}.{q_right[:i]}({q_right[i:]})'
