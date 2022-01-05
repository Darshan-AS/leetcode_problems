class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        s_people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        queue = []
        for h, k in s_people:
            queue.insert(k, [h, k])
        
        return queue
