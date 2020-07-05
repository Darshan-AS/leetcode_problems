class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])
        if s1_counter == s2_counter:
            return True
        
        for i in range(s1_len, s2_len):
            s2_counter[s2[i]] += 1
            x = s2[i - s1_len]
            if s2_counter[x] == 1:
                del s2_counter[x]
            else:
                s2_counter[x] -= 1
            
            if s1_counter == s2_counter:
                return True
        
        return False
