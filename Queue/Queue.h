#ifndef QUEUE_H
#define QUEUE_H

#include "QueueNode.h"

class Queue
{
private:


	QueueNode *first, *last;
	int size;

public:

	Queue();
	~Queue();
	Node* lookupNext();
	int lookupNextDepth();

	void popNode();
	void addNode(Node *, int);
	int getSize();

};

#endif
