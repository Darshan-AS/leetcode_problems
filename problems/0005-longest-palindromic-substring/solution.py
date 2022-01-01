class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher's Algorithm
        def expand_palindrome_around(seq: Sequence, center: int, radius: int = 0) -> int:
            n = len(seq)
            i, j = center - radius, center + radius
            while 0 <= i <= j < n and seq[i] == seq[j]:
                i, j = i - 1, j + 1
            return j - center - 1

        def palindrome_intervals(seq: Sequence):
            seq = "|".join(chain(("",), seq, ("",)))
            radius_map = [0] * len(seq)

            old_center, old_radius = -1, -1
            for center in range(len(seq)):
                
                radius = 0
                if center <= old_center + old_radius:
                    mirrored_center = old_center - (center - old_center)
                    mirrored_radius = radius_map[mirrored_center]
                    
                    old_end = old_center + old_radius
                    end = center + mirrored_radius
                    
                    max_radius = old_center + old_radius - center
                    
                    if end < old_end:
                        radius = mirrored_radius
                    elif end > old_end:
                        radius = max_radius
                    else:
                        radius = expand_palindrome_around(seq, center, mirrored_radius)
                else:
                    radius = expand_palindrome_around(seq, center)
                
                radius_map[center] = radius
                old_center, old_radius = max((old_center, old_radius), (center, radius), key=sum)

            return [((c - r) // 2, ((c + r) // 2) - 1) for c, r in enumerate(radius_map) if r]

        start, end = max(palindrome_intervals(s), key=lambda x: x[1] - x[0])
        return s[start : end + 1]
