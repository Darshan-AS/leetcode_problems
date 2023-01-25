class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def dist_from(node: int) -> dict[int, int]:
            dist = {node: 0}
            while node != -1  and (next_node := edges[node]) not in dist:
                dist[next_node] = dist[node] + 1
                node = next_node
            return dist
        
        dist_1, dist_2 = dist_from(node1), dist_from(node2)
        dist_common = ((max(dist_1[node], dist_2[node]), node) for node in dist_1.keys() & dist_2.keys())
        return min(dist_common, default=(0, -1))[1]

        
