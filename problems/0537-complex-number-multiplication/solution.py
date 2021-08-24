class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def make_complex(real: int, img: int) -> str:
            return f'{real}+{img}i'
        
        def unmake_complex(cpx: str) -> (int, int):
            real, img, *_ = cpx.split('+')
            return int(real), int(img[:-1])
        
        a1, b1 = unmake_complex(num1)
        a2, b2 = unmake_complex(num2)
        a, b = a1 * a2 - b1 * b2, a1 * b2 + b1 * a2
        return make_complex(a, b)
