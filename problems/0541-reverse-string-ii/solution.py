class Solution:
    def reverseStr(self, s_: str, k_: int) -> str:
        def split(s: str, k: int) -> List[str]:
            for i in range(0, len(s), k):
                yield s[i: i + k]
        
        def reverse(s: str) -> str:
           # return str(reversed(s))
            return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

                
        return ''.join(reverse(s[:k_]) + s[k_:] for s in split(s_, 2 * k_))
