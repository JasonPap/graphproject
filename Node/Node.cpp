#include <iostream>
#include "Node.h"

using namespace std;

Node::Node(int ID)
{
	id = ID;
	properties = NULL;
	links = NULL;
}

int Node::get_id()
{
	return id;
}