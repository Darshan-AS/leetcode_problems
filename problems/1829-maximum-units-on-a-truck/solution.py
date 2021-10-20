class Solution:
    def maximumUnits(self, box_types: List[List[int]], truck_size: int) -> int:
        total_units = 0
        for boxes, units in sorted(box_types, key=lambda x: x[::-1], reverse=True):
            if truck_size <= 0: break
            total_units += min(boxes, truck_size) * units
            truck_size -= boxes
        return total_units
