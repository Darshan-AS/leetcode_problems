from collections import deque, defaultdict

class Solution:

    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        neighbours = defaultdict(set)
        for word in word_list:
            for i in range(len(word)):
                neighbours[word[:i] + "*" + word[i + 1:]].add(word)
        
        queue = deque([(begin_word, 1)])
        seen = set()
        while queue:
            curr_word, steps = queue.popleft()
            if curr_word == end_word:
                return steps
            for i in range(len(curr_word)):
                for word in neighbours[curr_word[:i] + "*" + curr_word[i + 1:]]:
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, steps + 1))
        return 0
