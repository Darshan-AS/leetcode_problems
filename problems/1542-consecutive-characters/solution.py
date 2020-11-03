class Solution:
    def maxPower(self, s: str) -> int:
        max_power = power = 0
        curr_char = s[0]
        for i in s:
            if i != curr_char:
                curr_char = i
                power = 0
            power += 1
            max_power = max(max_power, power)
        return max_power
