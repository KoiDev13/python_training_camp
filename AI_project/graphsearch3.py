from searchAlgorithm import Graph


class Graph3(Graph):
    """Class Graph3 kế thừa từ class Graph."""
    def __init__(self, adjacency_list,heuristic):
        super().__init__(adjacency_list,heuristic)
        
adjacency_list_graph3 = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',1), ('D',5)],
    'C': [('A',4), ('B',1), ('D',3)],
    'D': [('B',5), ('C',3), ('E',8), ('F',3), ('G',9)],
    'E': [('D',8), ('G',2)],
    'F': [('D',3), ('G',5)],
    'G': [('E',2), ('F',5)]
}


heuristic_graph31 = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0
}

heuristic_graph32 = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0
}


print('Program start!')
print('-------------------------')

print('Graph 3 with heuristic 1:')
graph31 = Graph3(adjacency_list_graph3, heuristic_graph31)
graph31.a_star_algorithm('A', 'G')
graph31.greedy_algorithm('A', 'G')
graph31.ucs_algorithm('A', 'G')

print('-------------------------')
print('Graph 3 with heuristic 2:')
graph32 = Graph3(adjacency_list_graph3, heuristic_graph32)
graph32.a_star_algorithm('A', 'G')
graph32.greedy_algorithm('A', 'G')
graph32.ucs_algorithm('A', 'G')

print('-------------------------')
print('Program end!')