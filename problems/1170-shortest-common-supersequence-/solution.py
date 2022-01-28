class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def longest_common_subsequence(s1: str, s2: str) -> str:
            n1, n2 = len(s1), len(s2)
            
            dp = ['' for _ in range(n2 + 1)]
            
            for i, j in product(range(n1), range(n2)):
                k = j + 1
                prev = dp[0] if j == 0 else prev
                prev, dp[k] = dp[k], prev + s1[i] if s1[i] == s2[j] else max(dp[k - 1], dp[k], key=len)
            
            return dp[-1]
        
        def shortest_common_supersequence(s1: str, s2: str) -> iter:
            lcs = longest_common_subsequence(str1, str2)

            iter1, iter2 = iter(str1), iter(str2)
            for ch in chain(lcs, ('',)):
                ne_ch = partial(ne, ch)
                yield from chain(takewhile(ne_ch, iter1), takewhile(ne_ch, iter2), (ch,))
        
        return ''.join(shortest_common_supersequence(str1, str2))
