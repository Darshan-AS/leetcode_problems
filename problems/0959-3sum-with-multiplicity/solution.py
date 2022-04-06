class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        nums = sorted(arr)
        counter = Counter(nums)

        i, n = 0, len(nums)
        count = 0
        while i < n:
            j, k = i, n - 1 # j should be the leftmost index, hence j = i instead of j = i + 1
            
            while j < k:
                ni, nj, nk = nums[i], nums[j], nums[k]
                nsum = ni + nj + nk

                if nsum < target: j += counter[nj]
                elif nsum > target: k -= counter[nk]
                else:
                    if ni != nj != nk:      # Case 1: All the numbers are different
                        count += counter[ni] * counter[nj] * counter[nk]
                    elif ni == nj != nk:    # Case 2: The smaller two numbers are the same
                        count += counter[ni] * (counter[ni] - 1) * counter[nk] // 2 # math.comb(counter[ni], 2) * counter[nk]
                    elif ni != nj == nk:    # Case 3: The larger two numbers are the same
                        count += counter[ni] * counter[nj] * (counter[nj] - 1) // 2 # math.comb(counter[nj], 2) * counter[nk]
                    else:                   # Case 4: All the numbers are the same
                        count += counter[ni] * (counter[ni] - 1) * (counter[ni] - 2) // 6 # math.comb(counter[ni], 3)
                    
                    j += counter[nj]
                    k -= counter[nk]
            
            i += counter[ni]
        
        return count % 1_000_000_007

