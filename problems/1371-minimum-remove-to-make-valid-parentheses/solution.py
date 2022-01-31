class Solution:
    def minRemoveToMakeValid(self, s0: str) -> str:
        def balance_right(s: str, left: str, right: str) -> str:
            balance = 0

            for ch in s:
                if ch == left:
                    balance += 1
                elif ch == right:
                    if not balance: continue
                    balance -= 1

                yield ch
        
        s1 = ''.join(balance_right(s0, '(', ')'))
        s2 = ''.join(balance_right(reversed(s1), ')', '('))
        return ''.join(reversed(s2))
