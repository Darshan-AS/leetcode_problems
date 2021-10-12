from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len: return []
        
        s_counter, p_counter = Counter(s[:p_len]), Counter(p)
        indices = [0] if s_counter == p_counter else []
        
        for i in range(p_len, s_len):
            s_counter[s[i]] += 1
            x = s[i - p_len]
            # Not needed on python 3.10 and above as counter values with 0 will be ignored while comparing
            if s_counter[x] == 1:
                del s_counter[x]
            else:
                s_counter[x] -= 1
            
            if s_counter == p_counter:
                indices.append(i - p_len + 1)
        
        return indices
