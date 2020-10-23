class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [(nums[0], nums[0])]
        for i in nums[1:]:
            a, b = stack[-1]
            if i <= a:
                stack.append((i, i))
            elif i >= b:
                while stack and stack[-1][1] < i:
                    x, y = stack.pop()
                    a = min(a, x)
                if stack and stack[-1][0] < i < stack[-1][1]: return True
                stack.append((a, i))
            else:
                return True
        return False
