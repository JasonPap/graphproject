#include "listnode.h"
#include "listIterator.h"
#pragma once
class list
{
public:
	//functions
	list();
	~list();
	void Add(void*);
	int getLength();
	bool isEmpty();
	listIterator* getIterator();

private:
	int length;
	listnode* first_node;
};

