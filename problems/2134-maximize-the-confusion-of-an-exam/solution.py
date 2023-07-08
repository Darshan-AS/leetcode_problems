class Solution:
    def maxConsecutiveAnswers(self, answer_key: str, k: int) -> int:
        def max_streak(x: str) -> int:
            m_streak = streak = i = 0
            for j in range(len(answer_key)):
                if answer_key[j] == x: streak += 1
                while i <= j and streak > k: streak -= answer_key[i] == x; i += 1
                m_streak = max(m_streak, j - i + 1)
            return m_streak
        
        return max(map(max_streak, ('T', 'F')))
