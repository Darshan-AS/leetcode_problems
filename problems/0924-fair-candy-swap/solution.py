class Solution:
    def fairCandySwap(self, alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
        a_sum = sum(alice_sizes)
        b_sum = sum(bob_sizes)
        d = a_sum - b_sum
        
        b_set = set(bob_sizes)
        for a in alice_sizes:
            b = (2 * a - d) // 2
            if b in b_set:
                return [a, b]
        
