class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        w_chain = {}
        for w in sorted(words, key=len):
            w_chain[w] = max(w_chain.get(w[:j] + w[j + 1:], 0) for j in range(len(w))) + 1
        
        return max(w_chain.values())
        
