#include "QueueNode.h"
#include <iostream>

using namespace std;

QueueNode::QueueNode(Node * _komvos, QueueNode * previous, int _depth)
{
	komvos = _komvos;
	nextInQueue = NULL;
	previousInQueue = previous;
	depth = _depth;
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

QueueNode * QueueNode::getNext()
{
	return nextInQueue;
}

void QueueNode::setPrev(QueueNode * tempPrev)
{
	previousInQueue = tempPrev;
}

void QueueNode::setNext(QueueNode * tempNext)
{
	nextInQueue = tempNext;
}

int QueueNode::getDepth()
{
	return depth;
}