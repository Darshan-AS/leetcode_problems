class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        baskets = (-1, -1)
        max_picked = picked = 0
        i = 0
        for j in range(len(fruits)):
            if fruits[j] not in baskets:
                max_picked = max(max_picked, picked)
                baskets = (fruits[i], fruits[j])
                picked = j - i
            picked += 1
            i = j if fruits[i] != fruits[j] else i

        return max(max_picked, picked)
