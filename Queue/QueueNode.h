#ifndef QUEUENODE_H
#define QUEUENODE_H

#include "../Node/Node.h"

class QueueNode
{
private:

	QueueNode * nextInQueue;
	QueueNode * previousInQueue;
	Node * komvos;

public:

	QueueNode(Node* _komvos, QueueNode * prev);
	~QueueNode();
	Node * returnNode();
	QueueNode * getNext();
	void setPrev(QueueNode *);
	void setNext(QueueNode *);

};
#endif
