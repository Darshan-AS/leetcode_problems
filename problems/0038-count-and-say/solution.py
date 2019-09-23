class Solution:        
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for _ in range(1, n):
            count = 0
            current_ch = seq[0]
            next_seq_list = []
            for ch in seq:
                if ch == current_ch:
                    count += 1
                else:
                    next_seq_list.extend([str(count), current_ch])
                    current_ch = ch
                    count = 1
            next_seq_list.extend([str(count), current_ch])
            seq = ''.join(next_seq_list)
        return seq
