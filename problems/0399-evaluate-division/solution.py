from collections import deque

class Node:
    
    def __init__(self, var, connections=None):
        self.var = var
        self.connections = connections if connections else {}

class Solution:
    def make_graph(self, equations, values):
        graph = {}
        for eqn, val in zip(equations, values):
            numerator, denominator = eqn
            graph[numerator] = numerator_node = graph[numerator] if numerator in graph else Node(numerator)
            graph[denominator] = denominator_node = graph[denominator] if denominator in graph else Node(denominator)
            numerator_node.connections[denominator_node] = val
            denominator_node.connections[numerator_node] = 1 / val
        return graph
    
    def solve(self, graph, query):
        numerator, denominator = query
        if numerator not in graph or denominator not in graph:
            return -1.0
        
        visited = set()
        queue = deque([(graph[numerator], 1)])
        while queue:
            node, ans = queue.popleft()
            visited.add(node.var)
            if node.var == denominator:
                return ans
            
            for connection, value in node.connections.items():
                if connection.var not in visited:
                    queue.append((connection, ans * value))
        return -1.0
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.make_graph(equations, values)
        return list(map(lambda q: self.solve(graph, q), queries))
        
