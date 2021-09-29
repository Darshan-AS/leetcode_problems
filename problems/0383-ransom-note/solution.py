from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter, magazine_counter = Counter(ransomNote), Counter(magazine)
        return ransom_counter == (magazine_counter & ransom_counter)
