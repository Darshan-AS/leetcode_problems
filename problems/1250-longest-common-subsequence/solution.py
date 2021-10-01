class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def longest_common_subsequence(t1: int, t2: int) -> int:
            if t1 >= len(text1) or t2 >= len(text2):
                return 0

            if text1[t1] == text2[t2]:
                return 1 + longest_common_subsequence(t1 + 1, t2 + 1)
            else:
                return max(
                    longest_common_subsequence(t1 + 1, t2),
                    longest_common_subsequence(t1, t2 + 1),
                )
        
        return longest_common_subsequence(0, 0)
