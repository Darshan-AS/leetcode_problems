class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def stringify(i):
            s = ""
            if not i % 3: s += "Fizz"
            if not i % 5: s += "Buzz"
            return s if s else str(i)
        
        return list(map(stringify, range(1, n + 1)))
