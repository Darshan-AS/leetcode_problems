class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        def visit_rooms_from(room: int, visited: set[int]) -> set[int]:
            visited.add(room)
            
            for next_room in rooms[room]: 
                if next_room not in visited:
                    visit_rooms_from(next_room, visited)
            
            return visited
        
        return len(visit_rooms_from(0, set())) == len(rooms)
