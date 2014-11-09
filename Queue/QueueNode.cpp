#include "QueueNode.h"

QueueNode::QueueNode(Node * _komvos, QueueNode * previous )
{
	komvos = _komvos;
	nextInQueue = NULL;
	previousInQueue = previous;
}

QueueNode::~QueueNode()
{
	komvos = NULL;
	nextInQueue = NULL;
	previousInQueue = NULL;
}

Node * QueueNode::returnNode()
{
	return komvos;
}

Node * QueueNode::getNext()
{
	return next;
}

void QueueNode::setPrev(Node * tempPrev)
{
	previousInQueue = tempPrev;
}

void QueueNode::setNext(Node * tempNext)
{
	nextInQueue = tempNext;
}