__author__ = 'Jason'


class Node:
    def __init__(self, identifier, attributes, interests):
        self.id = identifier
        self.attributes = dict()
        self.interests = interests
        for attribute in attributes:
            self.attributes[attribute[0]] = attribute[1]
        self.links = []
