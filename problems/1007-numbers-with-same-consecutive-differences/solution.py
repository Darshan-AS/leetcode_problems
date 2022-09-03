class Solution:
    def numsSameConsecDiff(self, n_: int, k_: int) -> list[int]:
        def num_consec_diff(prefix: int, n: int, k: int):
            if n == 1: yield prefix; return
            
            last_digit = prefix % 10
            next_digit_candidates = {last_digit - k, last_digit + k}
            
            yield from chain.from_iterable(
                num_consec_diff(prefix * 10 + d, n - 1, k)
                for d in next_digit_candidates
                if 0 <= d <= 9
            )
        
        return list(chain.from_iterable(
            num_consec_diff(i, n_, k_)
            for i in range(1, 10)
        ))
