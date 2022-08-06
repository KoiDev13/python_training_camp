from collections import deque

class Graph:
    """Class defines đồ thị dưới dạng danh sách liền kề"""
    def __init__(self, adjacency_list,heuristic):
        """Khởi tạo graph."""
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        """Method để lấy tập biên O."""
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node):
        """ Thuật toán A* bao gồm f(m) = g(m)+h(m) min."""
        # open_list là list nodes đang được viếng thăm, chưa xác định tập biên
        # closed_list là list nodes đã được viếng thắm, xác định tập biên
        # Kiểu dữ liệu set: giá trị trong set là duy nhất, bất biến, và không lặp lại 
        open_list = set([start_node]) 
        closed_list = set([])
        count = 1

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        # Kiểu dữ liệu dictionary
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h[v] < g[n] + self.h[n]:
                    n = v

            if n == None:
                print('Astar Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Astar Path found: {}'.format(reconst_path))
                print('Astar Opened nodes:', count)
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count += 1   # count sẽ tăng thêm 1 nếu như node mới được add vào open_list
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Astar Path does not exist!')
        print('Astar Opened nodes:', count)
        return None

    def greedy_algorithm(self, start_node, stop_node):
        """ Thuật toán greedy bao gồm f(m) = h(m) min --> Bỏ g khỏi a star."""
        # open_list là list nodes đang được viếng thăm, chưa xác định tập biên
        # closed_list là list nodes đã được viếng thắm, xác định tập biên
        # Kiểu dữ liệu set: giá trị trong set là duy nhất, bất biến, và không lặp lại 
        open_list = set([start_node]) 
        closed_list = set([])
        count = 1

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        # Kiểu dữ liệu dictionary
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or self.h[v] < self.h[n]:
                    n = v

            if n == None:
                print('Greedy Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Greedy Path found: {}'.format(reconst_path))
                print('Greedy Opened nodes:', count)
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count += 1   # count sẽ tăng thêm 1 nếu như node mới được add vào open_list
                    parents[m] = n
                    # Vì không có g[m] nên bỏ đi phần còn lại của if

            open_list.remove(n)
            closed_list.add(n)

        print('Greedy Path does not exist!')
        print('Greedy Opened nodes:', count)
        return None    

    def ucs_algorithm(self, start_node, stop_node):
        """ Thuật toán UCS bao gồm f(m) = g(m) min. --> Bỏ h khỏi a star. """
        # open_list là list nodes đang được viếng thăm, chưa xác định tập biên
        # closed_list là list nodes đã được viếng thắm, xác định tập biên
        # Kiểu dữ liệu set: giá trị trong set là duy nhất, bất biến, và không lặp lại 
        open_list = set([start_node]) 
        closed_list = set([])
        count = 1

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        # Kiểu dữ liệu dictionary
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] < g[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('UCS Path found: {}'.format(reconst_path))
                print('UCS Opened nodes:', count)
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    count += 1   # count sẽ tăng thêm 1 nếu như node mới được add vào open_list
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('UCS Path does not exist!')
        print('UCS Opened nodes:', count)
        return None    