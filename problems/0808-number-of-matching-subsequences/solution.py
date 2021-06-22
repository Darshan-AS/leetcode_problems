class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices_map = defaultdict(list)
        for i, ch in enumerate(s):
            indices_map[ch].append(i)
        
        def is_subsequence(word: str) -> bool:
            start = 0
            for ch in word:
                ch_indicies = indices_map[ch]
                index = bisect_left(ch_indicies, start)
                if index >= len(ch_indicies):
                    return False
                start = ch_indicies[index] + 1
            return True
        
        return sum(map(is_subsequence, words))
