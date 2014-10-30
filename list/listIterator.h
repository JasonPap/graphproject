#include "listnode.h"
#pragma once
class listIterator
{
public:
	listIterator(listnode*);
	~listIterator();
	void*	getData();
	bool	next();	//move the iterator to the next listnode, retrun false if there is no next, else true

private:
	listnode* current_node;
};

