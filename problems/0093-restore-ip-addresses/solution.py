class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        points = (
            (i, j, k)
            for i in range(0 + 1, min(0 + 4, n))
            for j in range(i + 1, min(i + 4, n))
            for k in range(j + 1, min(j + 4, n))
        )

        is_valid_ip = lambda ip: all(map(lambda x: int(x) <= 255 and (len(x) == 1 or x[0] != '0'), ip))
        
        candidate_ips = ((s[:i], s[i:j], s[j:k], s[k:]) for i, j, k in points)
        valid_ips = filter(is_valid_ip, candidate_ips)
        return ['.'.join(ip) for ip in valid_ips]
