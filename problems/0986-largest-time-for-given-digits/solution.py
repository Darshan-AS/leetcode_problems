class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        hour_0_candidates = list(filter(lambda x: x in range(3), A))
        hour_0 = max(hour_0_candidates) if hour_0_candidates else -1
        if hour_0 == -1 : return ""
        A.remove(hour_0)
        
        hour_1_candidates = list(filter(lambda x: x in range(4), A)) if hour_0 == 2 else A.copy()
        hour_1 = max(hour_1_candidates) if hour_1_candidates else -1
        if hour_1 == -1 : return ""
        A.remove(hour_1)
        
        min_0_candidates = list(filter(lambda x: x in range(6), A))
        min_0 = max(min_0_candidates) if min_0_candidates else -1
        if min_0 == -1:
            if hour_1 < hour_0:
                hour_0, hour_1, min_0 = hour_1, max(A), hour_0
                A.remove(hour_1)
            else:
                return ""
        else:
            A.remove(min_0)
        
        min_1 = A[0]
        
        return f"{hour_0}{hour_1}:{min_0}{min_1}"
