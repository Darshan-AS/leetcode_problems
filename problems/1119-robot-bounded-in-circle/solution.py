from enum import Enum

class Solution:    
    class Pose:
        class Direction(Enum):
            N, E, W, S = 'N', 'E', 'W', 'S'
            
        directions = [
            Direction.N,
            Direction.E,
            Direction.S,
            Direction.W
        ]
        
        steps = {
            Direction.N: (0, 1),
            Direction.E: (1, 0),
            Direction.W: (-1, 0),
            Direction.S: (0, -1)
        }
        
        def __init__(self, x, y, d):
            self.x, self.y, self.d = x, y, d
            
        @property
        def position(self):
            return (self.x, self.y)
        
        @property
        def direction(self):
            return self.d
        
        def turn_left(self):
            self.d = self.directions[(self.directions.index(self.d) - 1) % 4]
            
        def turn_right(self):
            self.d = self.directions[(self.directions.index(self.d) + 1) % 4]
        
        def move_ahead(self):
            dx, dy = self.steps[self.d]
            self.x, self.y = self.x + dx, self.y + dy
            
    def isRobotBounded(self, instructions: str) -> bool:
        initial, final = self.Pose(0, 0, self.Pose.Direction.N), self.Pose(0, 0, self.Pose.Direction.N)
        
        for i in instructions:
            if i == 'L': final.turn_left()
            elif i == 'R': final.turn_right()
            elif i == 'G': final.move_ahead()
        
        return final.position == initial.position or final.direction != self.Pose.Direction.N
