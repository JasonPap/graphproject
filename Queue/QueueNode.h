#ifndef QUEUENODE_H
#define QUEUENODE_H

#include "../Node/Node.h"

class QueueNode
{
private:

	QueueNode * nextInQueue;
	QueueNode * previousInQueue;
	Node * komvos;

	int depth;

public:

	QueueNode(Node* _komvos, QueueNode * prev, int _depth);
	~QueueNode();
	Node * returnNode();
	QueueNode * getNext();
	void setPrev(QueueNode *);
	void setNext(QueueNode *);
	int getDepth();
};
#endif
