from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return list(map(lambda x: x[0], filter(lambda x: x[1] > 1, Counter(s[i: i + 10] for i in range(len(s) - 9)).items())))
