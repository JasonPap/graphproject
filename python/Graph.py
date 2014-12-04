__author__ = 'Jason'

from collections import deque


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

        while not nodes_to_expand:
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
        Return the length of the min path from start to end nodes, if there is no path return -1
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










