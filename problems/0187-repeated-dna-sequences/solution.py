class Solution:
    def findRepeatedDnaSequences(self, dna: str) -> list[str]:
        # Rolling hash based on Rabin-Karp
        def rolling_hashes(pattern_len: int, text_stream: Iterator, radix: int = 256, mod_q: int = 997, key=ord) -> Iterator[int]:
            m = pattern_len
            
            R, Q = radix, mod_q
            RM = pow(R, m - 1, Q)
            queue = deque(maxlen=m)
        
            h = 0
            for ch in text_stream:
                h = (h + Q - RM * queue[0] % Q) % Q if len(queue) >= m else h
                queue.append(key(ch))
                h = (h * R + queue[-1]) % Q
                yield h
        
        
        m = 10
        encoder = dict(zip('ACGT', range(4)))
        encoded_dna = map(encoder.get, dna)
        
        # hashes = islice(rolling_hashes(m, dna, mod_q=1_000_000_007), m - 1, None)
        hashes = islice(rolling_hashes(m, encoded_dna, radix=4, mod_q=1_000_000_007, key=hash), m - 1, None)
        repeated = []
        seen = defaultdict(int)
        
        for i, h in enumerate(hashes):
            seen[h] += 1
            if seen[h] == 2: repeated.append(dna[i: i + m])
        
        return repeated
