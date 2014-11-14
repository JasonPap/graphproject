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
	while(size != 0)
 	{
  		popNode();
 	}
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
	if (size > 1)
	{


		QueueNode * tempQN = first;

		first = first->getNext();
		size--;
		first->setPrev(NULL);

		delete tempQN;

	}
	else if(size == 1)
    {
        size--;
        delete first;
    }


	return;

}

void Queue::addNode(Node * temp, int depth)
{


	QueueNode * tempL = new QueueNode(temp, last, depth);
	if( size != 0 )
		last->setNext(tempL);
	last = tempL;
	if (size == 0)
	{
		first = tempL;
last = tempL;
	}
	size++;

}

int Queue::getSize()
{
	return size;
}

int Queue::lookupNextDepth()
{
	return first->getDepth();
}
