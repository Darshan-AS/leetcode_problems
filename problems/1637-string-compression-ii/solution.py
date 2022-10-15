class Solution:
    def getLengthOfOptimalCompression(self, s: str, k_: int) -> int:
        @cache
        def min_len_RLE(i: int, k: int, prev_ch: str='', prev_cnt: int=0) -> int:
            if k < 0: return inf
            if i >= len(s): return 0
            
            delete_len = min_len_RLE(i + 1, k - 1, prev_ch, prev_cnt)
            keep_len = (
                min_len_RLE(i + 1, k, prev_ch, prev_cnt + 1) + (prev_cnt in (1, 9, 99))
                if s[i] == prev_ch else
                min_len_RLE(i + 1, k, s[i], 1) + 1
            )
            
            return min(delete_len, keep_len)
        
        return min_len_RLE(0, k_)
