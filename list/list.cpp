#include <iostream>
#include "list.h"

using namespace std;


list::list()
{//list constructor
	length = 0;
	first_node = NULL;
}


list::~list()
{
    while(!isEmpty())
    {
        listnode* tmp = first_node->next;
        delete(first_node);
        first_node = tmp;
        length--;
    }
}


int list::getLength()
{
	return length;
}

bool list::isEmpty()
{
	if (length == 0)
		return true;
	else
		return false;
}

void list::Add(void* Data)
{
	if (length == 0)
	{
		first_node = new listnode(Data);
	}
	else
	{
		listnode* second_node = first_node;
		first_node = new listnode(Data);
		first_node->next = second_node;
	}
	length++;
}

listIterator* list::getIterator()
{//return an listIterator object or NULL if the list is empty
	if (!isEmpty())
	{
		listIterator* iterator = new listIterator(first_node);
		return iterator;
	}
	else
	{
		return NULL;
	}
}
