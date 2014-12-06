__author__ = 'Jason'

from Graph import Graph
from Node import Node
from Edge import Edge


def create_graph_from_file(filename):
    """
    Create a graph from a CSV file. Column[0] -> Column[1]
    :param filename: CSV filename
    :return: Graph
    """
    with open(filename, 'r') as input_file:
        first_line = input_file.readline()
        parameters = first_line.split('|')
        print 'creating graph: ' + parameters[0] + ' -> ' + parameters[1]
        graph = Graph()
        for line in input_file:
            if line[0] not in graph.dictionary:
                node = Node(line[0])
                graph.insert_node(node)

            if line[1] not in graph.dictionary:
                node = Node(line[1])
                graph.insert_node(node)

            edge = Edge(line[1])
            graph.insert_edge(line[0], edge)

    return graph


def create_reverse_graph_from_file(filename):
    """
    Create a graph from a CSV file. Column[1] -> Column[0]
    :param filename: CSV filename
    :return: Graph
    """
    with open(filename, 'r') as input_file:
        first_line = input_file.readline()
        parameters = first_line.split('|')
        print 'creating graph: ' + parameters[1] + ' -> ' + parameters[0]
        graph = Graph()
        for line in input_file:
            if line[0] not in graph.dictionary:
                node = Node(line[0])
                graph.insert_node(node)

            if line[1] not in graph.dictionary:
                node = Node(line[1])
                graph.insert_node(node)

            edge = Edge(line[0])
            graph.insert_edge(line[1], edge)

    return graph


def populate_person_graph(graph, person_data_file):
    """
    This functions takes a person knows person graph and populate the nodes with information from the file given
    :param person_data_file: a CSV file with information about the persons
    :param graph: a person knows person graph
    """
    with open(person_data_file) as input_file:
        first_line = input_file.readline()
        parameters = first_line.split('|')

        for person in input_file:
            person_data = person.split('|')
            node = graph.lookup_node(person_data[0])
            index = 0
            for attribute in person_data[1:]:
                node.attributes[parameters[index]] = attribute
                index += 1

    return
