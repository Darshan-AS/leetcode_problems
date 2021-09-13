class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {ch: 0 for ch in 'balon'}
        for ch in text:
            if ch in counter:
                counter[ch] += 1
        
        return min(counter[ch] // w for ch, w in zip('balon', (1, 1, 2, 2, 1)))
