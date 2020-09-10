from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = defaultdict(int)
        
        bulls = cows = 0
        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                count[s_ch] += 1
                count[g_ch] -= 1
                if count[s_ch] <= 0: cows += 1
                if count[g_ch] >= 0: cows += 1
        
        return f'{bulls}A{cows}B'
