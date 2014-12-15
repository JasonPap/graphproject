__author__ = 'Jason'


class Edge:
    def __init__(self, destination, properties):
        self.edge_end = destination
        self.properties = dict()
        for propertie in properties:
            self.properties[propertie[0]] = propertie[1]