from searchAlgorithm import Graph


class Graph1(Graph):
    """Class Graph1 kế thừa từ class Graph."""
    def __init__(self, adjacency_list,heuristic):
        super().__init__(adjacency_list,heuristic)
        
adjacency_list_graph1 = {
    'S': [('F', 3), ('A', 2), ('B', 1)],
    'F': [('G', 6)],
    'A': [('C', 2), ('D', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'E': [],
    'G': []
}


heuristic_graph1 = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0,
}

print('Program start!')
print('-------------------------')
graph1 = Graph1(adjacency_list_graph1, heuristic_graph1)
graph1.a_star_algorithm('S', 'G')
graph1.greedy_algorithm('S', 'G')
graph1.ucs_algorithm('S', 'G')
print('-------------------------')
print('Program end!')