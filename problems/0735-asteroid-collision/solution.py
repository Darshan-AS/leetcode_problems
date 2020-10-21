class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i < 0:
                while stack and 0 <= stack[-1] < abs(i):
                    stack.pop()
                if stack and stack[-1] == abs(i):
                    stack.pop()
                    continue
                if not stack or stack[-1] < 0: stack.append(i)
            else:
                stack.append(i)
        return stack
