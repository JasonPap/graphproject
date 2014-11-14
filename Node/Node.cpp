#include <iostream>
#include "Node.h"
#include "../Edge/Edge.h"

using namespace std;

Node::Node(int ID)
{
	id = ID;
	properties = NULL;
	links = new list();
}

Node::~Node()
{
	if(properties != NULL)
		delete properties;

	if(links != NULL)
    {
        if(!links->isEmpty())
        {
            listIterator* it = links->getIterator();
            Edge* e = (Edge*)it->getData();
            delete(e);
            while(it->getData())
            {
                e = (Edge*)it->getData();
                delete(e);
            }
            delete(it);
        }

        delete links;
    }

}

int Node::get_id()
{
	return id;
}
