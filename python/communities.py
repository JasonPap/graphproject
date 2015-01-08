from multiprocessing import Pool, Queue
import multiprocessing
from FileOperations import *


def find_top_n_communities(n):
    """
    :param n: how many forums will be returned
    :return: list of forums
    """
    forum_size = dict()
    with open("forum_hasMember_person.csv", 'r') as input_file:
        first_line = input_file.readline()
        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if int(line[0]) not in forum_size:
                forum_size[int(line[0])] = 1
            else:
                forum_size[int(line[0])] += 1

    l_forums = []
    for forum in forum_size:
        l_forums.append((forum_size[forum], forum))
    l_forums.sort()
    l_forums.reverse()
    r_list = []
    for x in l_forums:
        r_list.append(x[1])

    return r_list[:n]


def create_communities_graphs(top_forums, pkp_graph, proc_pool):
    forum_has_member = create_graph_from_file("forum_hasMember_person.csv")
    # proc_pool = Pool(processes=multiprocessing.cpu_count())
    arg = []
    for forum in top_forums:
        arg.append((forum, pkp_graph, forum_has_member))
    result = proc_pool.map(create_community, arg)
    return result


def create_community(arg):
    forum_id = arg[0]
    pkp_graph = arg[1]
    forum_has_member = arg[2]
    forum_members = []
    for edge in forum_has_member.dictionary[forum_id].links:
        forum_members.append(edge.edge_end)

    community_graph = Graph()
    community_graph.fill_from_list(forum_members, pkp_graph)
    return community_graph



