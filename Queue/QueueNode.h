

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
	Node * getNext();
	void setPrev();
	void setNext();

};