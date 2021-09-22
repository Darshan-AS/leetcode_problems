class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charset = string.ascii_lowercase
        charset_count = len(charset)
        n1, n2 = len(s1), len(s2)
        
        s1_counter = {ch: 0 for ch in charset}
        for ch in s1:
            s1_counter[ch] += 1
        
        s2_window_counter = {ch: 0 for ch in charset}
        for ch in s2[:n1]:
            s2_window_counter[ch] += 1
            
        same_ch_counts = sum(s1_counter[ch] == s2_window_counter[ch] for ch in charset)
        for j in range(n1, n2):
            i = j - n1
            first, last = s2[i], s2[j]
            if same_ch_counts == charset_count:
                return True
            
            s2_window_counter[last] += 1
            if s2_window_counter[last] == s1_counter[last]:
                same_ch_counts += 1
            elif s2_window_counter[last] - 1 == s1_counter[last]:
                same_ch_counts -= 1
            
            s2_window_counter[first] -= 1
            if s2_window_counter[first] == s1_counter[first]:
                same_ch_counts += 1
            elif s2_window_counter[first] + 1 == s1_counter[first]:
                same_ch_counts -= 1
            

                    
        return same_ch_counts == charset_count
        
