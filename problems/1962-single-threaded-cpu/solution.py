class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        remaining_ts = sorted((t, i) for i, t in enumerate(tasks))

        indices = []
        j = 0
        t = remaining_ts[j][0][0]
        available_ts = []
        while len(indices) != len(tasks):
            t = t if available_ts else max(t, remaining_ts[j][0][0])
            while j < len(remaining_ts) and remaining_ts[j][0][0] <= t:
                (et, pt), i = remaining_ts[j]
                heappush(available_ts, (pt, i, et))
                j += 1
            pt, i, et = heappop(available_ts)
            indices.append(i)
            t += pt
        
        return indices

