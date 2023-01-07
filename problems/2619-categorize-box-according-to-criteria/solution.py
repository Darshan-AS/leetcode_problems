class Solution:
    def categorizeBox(self, l: int, w: int, h: int, m: int) -> str:
        bulky = any(x >= 10000 for x in (l, w, h)) or l * w * h >= 10 ** 9
        heavy = m >= 100
        
        match (bulky, heavy):
            case (True, True): return "Both"
            case (False, False): return "Neither"
            case (True, False): return "Bulky"
            case (False, True): return "Heavy"
