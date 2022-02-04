class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        s_people = sorted(people)
        boats_count = 0
        
        i, j = 0, len(s_people) - 1
        while i <= j:
            if s_people[j] + s_people[i] <= limit: i += 1
            j -= 1
            boats_count += 1
        
        return boats_count
