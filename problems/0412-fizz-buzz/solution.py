class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        stringify = lambda i: ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i)
        return list(map(stringify, range(1, n + 1)))
