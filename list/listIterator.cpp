#include <iostream>
#include "listIterator.h"

using namespace std;

listIterator::listIterator(listnode* Node)
{
	current_node = Node;
}


listIterator::~listIterator()
{
}

void* listIterator::getData()
{
	return current_node->GetValue();
}

bool listIterator::next()
{
	if (current_node == NULL)
		return false;

	if (current_node->next == NULL)
		return false;
	
	//else 
	current_node = current_node->next;
	return true;
}