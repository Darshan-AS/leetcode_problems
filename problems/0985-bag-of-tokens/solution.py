class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        power, max_score, score = P, 0, 0
        i, j = 0, len(tokens) - 1
        while i <= j:
            while i <= j and power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            max_score = max(max_score, score)
            
            if not score:
                return max_score
            power += tokens[j]
            score -= 1
            j -= 1
        return max_score
