#include "../GenArray/GenArray.h"
#include "../Node/Node.cpp"

class HashMap
{

private:
	int split_index;
	int original_size;
	int round;
	GenArray* hashTable;
	
	int hash(int );
	int next_hash(int );
	
public:
	HashMap(int start_size, int bucket_cells);
	bool insertNode(Node* );
	bool insertEdge();
};
