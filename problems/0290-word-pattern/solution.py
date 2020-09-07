class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        p, s = pattern, string.split()
        if len(p) != len(s):
            return
        
        match, words = dict(), set()
        for ch, word in zip(p, s):
            if ch in match and match[ch] != word: return False
            if ch not in match and word in words: return False
            match[ch] = word
            words.add(word)
        return True
