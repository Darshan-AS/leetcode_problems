from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict, guess_dict = defaultdict(int), defaultdict(int)
        
        bulls = 0
        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                secret_dict[s_ch] += 1
                guess_dict[g_ch] += 1
        
        cows = 0
        for s_ch in secret_dict:
            cows += min(secret_dict[s_ch], guess_dict[s_ch])
        
        return f'{bulls}A{cows}B'
