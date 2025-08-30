class Graph:
    def __init__(self, n):
        self.list = [[]for i in range(n)]
        self.n = n
    def create_edge(self, n1, n2):
        self.list[n1].append(n2)
        self.list[n2].append(n1)
    def bfs(self, source):
        visited = [False] * self.n
        result = []
        queue = []
        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            s = queue.pop(0)
            result.append(s)
            for node in self.list[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        print(result)
graph = Graph(4)
graph2 = Graph(8)
graph2.create_edge(0,1)
graph2.create_edge(0,2)
graph2.create_edge(0,3)
graph2.create_edge(1,4)
graph2.create_edge(1,5)
graph2.create_edge(2,6)
graph2.create_edge(3,7)
graph2.bfs(0)
print(graph.list)

