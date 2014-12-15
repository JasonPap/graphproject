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
    graph = Graph()
    with open(filename, 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')
        print 'creating graph: ' + parameters[0] + ' -> ' + parameters[1]

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if int(line[0]) not in graph.dictionary:
                node = Node(int(line[0]), [], [])
                graph.insert_node(node)

            if int(line[1]) not in graph.dictionary:
                node = Node(int(line[1]), [], [])
                graph.insert_node(node)

            edge = Edge(int(line[1]), [])
            graph.insert_edge(int(line[0]), edge)

    return graph


def create_reverse_graph_from_file(filename):
    """
    Create a graph from a CSV file. Column[1] -> Column[0]
    :param filename: CSV filename
    :return: Graph
    """
    graph = Graph()
    with open(filename, 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')
        print 'creating graph: ' + parameters[1] + ' -> ' + parameters[0]

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if line[0] not in graph.dictionary:
                node = Node(int(line[0]), [], [])
                graph.insert_node(node)

            if line[1] not in graph.dictionary:
                node = Node(int(line[1]), [], [])
                graph.insert_node(node)

            edge = Edge(int(line[0]), [])
            graph.insert_edge(int(line[1]), edge)

    return graph


def populate_person_graph(graph, person_data_file, person_interests_file):
    """
    This functions takes a person knows person graph and populate the nodes with information from the file given
    :param person_data_file: a CSV file with information about the persons
    :param graph: a person knows person graph
    """
    with open(person_data_file) as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for person in input_file:
            person = person.rstrip('\n')
            person_data = person.split('|')
            node = graph.lookup_node(int(person_data[0]))
            if node is not None:
                index = 1
                for attribute in person_data[1:]:
                    node.attributes[parameters[index]] = attribute
                    index += 1

    with open(person_interests_file) as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            node = graph.lookup_node(int(line[0]))
            if node is not None:
                node.interests.append(int(line[1]))

    return


def create_dictionary_from_file(filename):
    """
    Create a dictionary from a CSV file, first column must be the key, second column the value
    :param filename: the name of a CSV file to be read
    :return: dict
    """
    dictionary = dict()
    with open(filename) as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')
        print 'creating dictionary[' + parameters[0] + '] = ' + parameters[1]

        for line in input_file:
            line = line.rstrip('\n')
            values = line.split('|')
            dictionary[int(values[0])] = int(values[1])

    return dictionary