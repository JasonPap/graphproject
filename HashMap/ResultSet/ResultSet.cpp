#include <iostream>
#include "ResultSet.h"

using namespace std;

ResultSet::ResultSet(Node* n)
{
    visited_nodes = new list();
    nodes_to_expand = new list();
    visited_nodes->Add(n);
    nodes_to_expand->Add(n);
}

Result* get_next()
{

    //get one node from nodes to expand (oxi remove, apla get)

    //for each link in its list

    ///if the node pointed is on the visited nodes SKIP
    ///else add it to visited and to nodes to expand

    //if links list end reached then remove node from nodes to expand

    //return distance and node ID
    int node_id, distance;
    return new Result(node_id,distance);
}

