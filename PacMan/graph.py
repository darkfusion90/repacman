import sys


class Graph:
    def __init__(self, v):
        self.vertices_count = v
        self.vertices = [i for i in range(v)]
        self.adj_mat = [[0 for _ in range(v)] for _ in range(v)]

    def connect_all(self):
        self.adj_mat = []
        for i in range(self.vertices_count):
            raw_mat = []
            for j in range(self.vertices_count):
                raw_mat.append(0 if i == j else 1)
            self.adj_mat.append(raw_mat)

    def add_edge(self, u, v, weight=1, ordered=False):
        #print("ADDING EDGE: (u: {}, v: {})".format(u, v))
        self.adj_mat[u][v] = weight
        if not ordered:
            self.adj_mat[v][u] = weight

    def print_graph(self):
        for i in range(self.vertices_count):
            for j in range(self.vertices_count):
                print(self.adj_mat[i][j], end=' ')
            print()

    def breadth_first_search(self, src, dest):
        visited = [False]*self.vertices_count
        distance = [sys.maxsize]*self.vertices_count
        previous_cell = [-1]*self.vertices_count

        queue = []

        visited[src] = True
        distance[src] = 0
        queue.append(src)

        while not len(queue) == 0:
            u = queue[0]
            queue.remove(u)
            for v in range(len(self.adj_mat[u])):
                if not visited[v] and self.adj_mat[u][v] != 0:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    previous_cell[v] = u
                    queue.append(v)

        return previous_cell

    def get_shortest_path(self, src, dest):
        return self.breadth_first_search(src, dest)

