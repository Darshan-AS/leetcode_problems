class Solution:
    def reverseWords(self, s_: str) -> str:        
        def reverse(s: str) -> str:
           # return ''.join(reversed(s))
            return ''.join(s[i] for i in range(len(s) - 1, -1, -1))
   
        return ' '.join(reverse(s) for s in s_.split(' '))
