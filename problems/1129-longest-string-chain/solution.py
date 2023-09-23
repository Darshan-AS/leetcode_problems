class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        return max(reduce(
            lambda a, w: setitem(a, w, max(a.get(w[:j] + w[j + 1:], 0) for j in range(len(w))) + 1) or a,
            sorted(words, key=len),
            {}, # w_chain (Longest chain for given word w)
        ).values())
        
