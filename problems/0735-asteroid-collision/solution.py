class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 < (j := stack[-1]):
                if j < -i:
                    stack.pop()
                elif j == -i:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(i)
        return stack
