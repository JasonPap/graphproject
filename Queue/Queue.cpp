#include "Queue.h"
#include <iostream>

using namespace std;

Queue::Queue()
{
	first = NULL;
	last = NULL;
	size = 0;
}

Queue::~Queue()
{
	first = NULL;
	last = NULL;
}

Node * Queue::lookupNext()
{
	if (size != 0)
		return (first->returnNode());
	else
		return NULL;
}


void Queue::popNode()
{
	if (size != 0)
	{

		
		QueueNode * tempQN = first;

		first = first->getNext();
		size--;
		first->setPrev(NULL);

		delete tempQN;

	}


	return;

}

void Queue::addNode(Node * temp)
{


	QueueNode * tempL = new QueueNode(temp, last);
	if( size != 0 )
		last->setNext(tempL);
	last = tempL;
	if (size == 0)
	{
		first = tempL;
	}
	size++;

}

int Queue::getSize()
{
	return size;
}
