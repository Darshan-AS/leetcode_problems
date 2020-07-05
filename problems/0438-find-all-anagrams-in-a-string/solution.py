from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        
        p_counter = Counter(p)
        s_counter = Counter(s[:p_len])
        
        indices = [0] if p_counter == s_counter else []
        for i in range(p_len, s_len):
            s_counter[s[i]] += 1
            x = s[i - p_len]
            if s_counter[x] == 1:
                del s_counter[x]
            else:
                s_counter[x] -= 1
            
            if p_counter == s_counter:
                indices.append(i - p_len + 1)
        
        return indices
