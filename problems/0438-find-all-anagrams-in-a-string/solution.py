class Solution:
    def findAnagrams(self, s2: str, s1: str) -> list[int]:
        n1, n2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(islice(s2, n1))
        
        eq_count = sum(c1[ch] == c2[ch] for ch in c1)

        starts = [0] if eq_count == len(c1) else []
        for i in range(n1, n2):
            fst, lst = s2[i - n1], s2[i]

            if c1[lst] and c2[lst] == c1[lst]: eq_count -= 1
            c2[lst] += 1
            if c1[lst] and c2[lst] == c1[lst]: eq_count += 1

            if c1[fst] and c2[fst] == c1[fst]: eq_count -= 1
            c2[fst] -= 1
            if c1[fst] and c2[fst] == c1[fst]: eq_count += 1

            if eq_count == len(c1): starts.append(i - n1 + 1)

        return starts
