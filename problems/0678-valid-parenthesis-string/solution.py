class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for i in s:
            low += 1 if i == '(' else -1
            high += -1 if i == ')' else 1
            if high < 0:
                break
            low = max(low, 0)
        return low == 0
