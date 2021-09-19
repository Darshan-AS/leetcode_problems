class Solution:
    def reverseWords(self, s_: str) -> str:        
        def split(s: str, sub_s: str) -> List[str]:
            k = 0
            word = []
            while k < len(s):
                
                i, j = k, 0
                while j < len(sub_s):
                    if s[i] != sub_s[j]:
                        break
                    i, j = i + 1, j + 1
                
                if j == len(sub_s):
                    yield ''.join(word)
                    word = []
                    k = i
                else:
                    word.extend(s[k: i + 1])
                    k = i + 1
            
            yield ''.join(word)
        
        def reverse(s: str) -> str:
           # return ''.join(reversed(s))
            return ''.join(s[i] for i in range(len(s) - 1, -1, -1))
        
        print(list(split(s_, ' ')))
        return ' '.join(reverse(s) for s in split(s_, ' '))
