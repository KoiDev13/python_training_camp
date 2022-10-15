from searchAlgorithm import Graph


class Graph2(Graph):
    """Class Graph2 kế thừa từ class Graph."""
    def __init__(self, adjacency_list,heuristic):
        super().__init__(adjacency_list,heuristic)
        
adjacency_list_graph2 = {
    'S': [('F',1), ('H',1)],
    'H': [('K',1)],
    'K': [('C',1)],
    'C': [('A',1)],
    'A': [('B',1)],
    'B': [('D',1)],
    'D': [('E',1), ('M',1)],
    'E': [('D',1), ('N',1)],
    'N': [('E',1), ('M',1)],
    'M': [('D',1), ('N',1), ('G',1)],
    'F': [('P',1)],
    'P': [('Q',1)],
    'Q': [('R',1)],
    'R': [('T',1)],
    'T': [('G',1)],
    'G': []
}


heuristic_graph2 = {
    'S': 4,
    'H': 3,
    'K': 2,
    'C': 3,
    'A': 4,
    'B': 3,
    'D': 2,
    'E': 3,
    'N': 2,
    'M': 1,
    'F': 5,
    'P': 4,
    'Q': 3,
    'R': 2,
    'T': 1,
    'G': 0
}

print('Program start!')
print('-------------------------')
graph2 = Graph2(adjacency_list_graph2, heuristic_graph2)
graph2.a_star_algorithm('S', 'G')
graph2.greedy_algorithm('S', 'G')
graph2.ucs_algorithm('S', 'G')
print('-------------------------')
print('Program end!')