#include <iostream>
#include "ResultSet.h"

using namespace std;

ResultSet::ResultSet(Node* n)
{
    visited_nodes = new list();
    nodes_to_expand = new Queue();
    visited_nodes->Add(n);
    nodes_to_expand->addNode(n);
}

Result* ResultSet::get_next()
{
    bool searching = true;
    Result* return_value = NULL;

    while(searching && nodes_to_expand->getSize() > 0)
    {
        //get one node from nodes to expand (oxi remove, apla get)
        Node* expand_node = nodes_to_expand->lookupNext();
        int expand_node_id = expand_node->get_id();

        if (expand_node->links->isEmpty())
        {
            //remove expand node from expand Queue
            nodes_to_expand->getNode();
        }
        else
        {
            //for each link in its list
            listIterator* links = expand_node->links->getIterator();
            bool unvisited_node_found = false;

            while(!unvisited_node_found)
            {
                Node* new_node = (Node*)links->getData();
                int new_node_id = new_node->get_id();

                if(contains(visited_nodes,new_node_id))
                {///if the node pointed is on the visited nodes SKIP
                    if(links->next() == false) ///na ginei elenxos
                    ///an telos tis listas tote break
                    {
                        nodes_to_expand->getNode();//remove node
                        break;
                    }
                }
                else
                {///else add it to visited and to nodes to expand
                    visited_nodes->Add(new_node);
                    nodes_to_expand->addNode(new_node);

                    int distance = depth + 1;
                    return_value = new Result(new_node_id,distance);

                    unvisited_node_found = true;
                    searching = false;
                }
            }
            delete (links);
            //if links list end reached then remove node from nodes to expand

            //return distance and node ID

        }


    }

    return return_value;
}

bool ResultSet::contains(list* l, int id)
{
    if(l->isEmpty())
        return false;
    listIterator* it = l->getIterator();
    bool found = false;
    while(!found)
    {
        Node* n = (Node*)it->getData();
        if(n->get_id()==id)
        {
            delete(it);
            return true;
        }
        else
        {
            if(it->next() == false)
            {
                delete(it);
                return false;
            }

        }

    }
}
