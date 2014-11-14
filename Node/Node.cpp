#include <iostream>
#include "Node.h"

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
        delete links;
    }

}

int Node::get_id()
{
	return id;
}
