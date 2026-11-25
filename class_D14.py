class GRAPH:
    def __init__(self):
        self.vertex= []
        self.edges= []

    def display(self):
        pass

    def addvertex(self,vertex):
        if vertex not in self.vertex:
            self.vertex.append(vertex)


    def addEdges(self,s,d,w):
        if s in self.vertex and d in self.vertex:
            self.edges.append([s,d,w])


    def bellman_ford_algo(self,vertex):
        if vertex in self.vertex:
            dist= {i: float('inf') for i in self.vertex}
            dist[vertex]=0

            for _ in range(len(self.vertex)-1):
                for s,d,w in self.edges:
                    if dist[d]>dist[s]+w:
                        dist[d]= dist[s] +w
            self.display(dist)
        else:
            print('vertex doesnt exist')


gh= GRAPH()
gh.addvertex('A')
gh.addvertex('B')
gh.addvertex('C')
gh.addvertex('D')
gh.addvertex('E')
gh.bellman_ford_algo()