__author__ = 'Jason'

from collections import deque
from Node import Node
from Edge import Edge


class Graph:
    def __init__(self):
        self.dictionary = dict()
        self.number_of_nodes = 0
        self.number_of_edges = 0

    def insert_node(self, node):
        """
        Insert a node in the Graph
        :type node: Node
        """
        self.dictionary[node.id] = node
        self.number_of_nodes += 1

    def insert_edge(self, node_id, edge):
        """
        Insert an edge to a node with id = start if there is a node with that id
        :rtype : bool
        :param node_id: int
        :param edge: Edge
        """
        if node_id in self.dictionary:
            node = self.dictionary[node_id]
            node.links.append(edge)
            self.dictionary[node_id] = node
            self.number_of_edges += 1
            return True
        else:
            return False

    def lookup_node(self, node_id):
        """
        Return the Node with id = node_id if there is one in the Graph
        :rtype : Node
        :param node_id: int
        """
        if node_id in self.dictionary:
            return self.dictionary[node_id]
        else:
            return None

    def graph_bfs(self, start_node_id):
        """
        Generator that gives the distance of every node in the same connected component where the starting node is
        :param start_node_id: node ID to start the BFS
        :return: tuples (node_id, distance)
        """
        if start_node_id not in self.dictionary:
            return

        visited_nodes = [start_node_id]
        nodes_to_expand = deque([(start_node_id, 0)])

        while nodes_to_expand:
            current_node = self.dictionary[nodes_to_expand[0][0]]
            current_node_distance = nodes_to_expand[0][1]
            current_node_links = current_node.links
            for edge in current_node_links:
                if edge.edge_end not in visited_nodes:
                    visited_nodes.append(edge.edge_end)
                    new_distance = current_node_distance + 1
                    nodes_to_expand.append((edge.edge_end, new_distance))
                    yield (edge.edge_end, new_distance)
            nodes_to_expand.popleft()

    def reach_node_1(self, start, end):
        """
        Return the length of the min path from start to end nodes, if there is no path return -1. Use BFS algorithm.
        :param start: int
        :param end: int
        :rtype : int
        """
        if start not in self.dictionary:
            print 'Node ' + start + ' is not in the graph'
            return -1
        elif end not in self.dictionary:
            print 'Node ' + end + ' is not in the graph'
            return -1

        bfs_generator = self.graph_bfs(start)
        for result in bfs_generator:
            if result[0] == end:
                return result[1]

        return -1

    def reach_node_n(self, start):
        """
        Generator that gives the distance of every node, if there is no path returned distance is -1 (node_id, distance)
        :rtype : (int, int)
        :param start: int
        """
        if start not in self.dictionary:
            print 'Node ' + start + ' is not in the graph'
            return

        bfs_generator = self.graph_bfs(start)
        attainable_nodes = []
        for result in bfs_generator:
            attainable_nodes.append(result[0])
            yield (result[0], result[1])

        for node_id in self.dictionary:
            if node_id not in attainable_nodes:
                yield (node_id, -1)

        return

    def reach_node_1_dual(self, start, end):
        """
        Return the length of the min path from start to end nodes, if there is no path return -1. Use BFS algorithm from
        both nodes
        :param start: int
        :param end: int
        :return: int
        """
        if start not in self.dictionary:
            print 'Node ' + start + ' is not in the graph'
            return -1
        elif end not in self.dictionary:
            print 'Node ' + end + ' is not in the graph'
            return -1

        bfs_generator_start = self.graph_bfs(start)
        bfs_generator_end = self.graph_bfs(end)
        path_found = False

        visited_nodes_from_start = dict()
        visited_nodes_from_start[start] = 0
        visited_nodes_from_end = dict()
        visited_nodes_from_end[end] = 0

        while not path_found:
            result = next(bfs_generator_start)
            if result is not None:
                visited_nodes_from_start[result[0]] = result[1]
                if result[0] in visited_nodes_from_end:
                    path_length = visited_nodes_from_start[result[0]] + visited_nodes_from_end[result[0]]
                    return path_length
            else:
                return -1

            result = next(bfs_generator_end)
            if result is not None:
                visited_nodes_from_end[result[0]] = result[1]
                if result[0] in visited_nodes_from_start:
                    path_length = visited_nodes_from_end[result[0]] + visited_nodes_from_start[result[0]]
                    return path_length
            else:
                return -1

        return

    def fill_from_list(self, persons_list, person_knows):

        for person_id in persons_list:
            node = person_knows.lookup_node(person_id)
            new_node = Node(person_id, [], [])
            new_node.attributes.extend(node.attributes)
            new_node.interests.extend(node.interests)
            self.insert_node(new_node)
            for edge in node.links:
                if edge.edge_end in persons_list:
                    new_edge = Edge(edge.edge_end, [])
                    self.insert_edge(person_id, new_edge)

        return

    def get_node_ids(self):
        node_ids = []
        for i in self.dictionary:
            node_ids.append(i)
        return node_ids

    def dijkstra_shortest_paths_from(self, start_node_id, end_node_id):
        """
        Generator of all shortest pats from start to end nodes
        :param start_node_id:
        :param end_node_id:
        :return:
        """
        dist = dict()
        path = dict()
        path[start_node_id] = []
        nodes_to_expand = deque()
        nodes_to_expand.append(start_node_id)
        for node_id in self.dictionary:
            dist[node_id] = float("inf")
            path[node_id] = []

        dist[start_node_id] = 0

        while nodes_to_expand:
            node_id = nodes_to_expand.popleft()
            if node_id == end_node_id:
                return
            for edge in self.lookup_node(node_id).links:
                neighbour = edge.edge_end
                nodes_to_expand.append(neighbour)
                alt = dist[node_id] + 1
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    path[neighbour] = path[node_id] + [neighbour]
                    if neighbour == end_node_id:
                        yield path[neighbour]

        return