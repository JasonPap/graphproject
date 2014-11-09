#include "Queue.h"

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
		return (returnNode);
	else
		return NULL;
}

Node * Queue::getNode()
{
	if (size != 0)
	{
		Node * temp = first->returnNode();
		QueueNode * tempQN = first;

		first = first->getNext();
		size--;
		first->setPrev(NULL);

		delete tempQN;

		return temp;
	}
	else
	{
		return NULL;
	}

}

void Queue::addNode(Node * temp)
{

	Node * tempL = new QueueNode(temp, last);
	last->setNext(tempL);
	last = tempL;
	if (size == 0)
	{
		first = tempL;
	}
	size++;

}