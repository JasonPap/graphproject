

class Queue
{
private:

	QueueNode * first, last;
	int size;

public:

	Queue();
	~Queue();
	Node* lookupNext();
	Node* getNode();
	void addNode(Node *);

};