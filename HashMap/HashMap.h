#include "../GenArray/GenArray.h"
#include "../Node/Node.cpp"

class HashMap
{

private:
	int split_index;
	int original_size;
	int round;
	int bucket_cells; //number of cells per bucket at start
	GenArray* hashTable;

	int hash(int );
	int next_hash(int );

	bool insert_into_array(Node*,GenArray*);
	bool split();
public:
	(Node *) lokupNode(int );
	HashMap(int start_size,int bucket_cells);
	bool insertNode(Node* );
	bool insertEdge();
};
