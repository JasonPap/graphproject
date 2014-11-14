#ifndef HASHMAP_H
#define HASHMAP_H

#include "../GenArray/GenArray.h"
#include "../Node/Node.h"
#include "../Edge/Edge.h"
#include "./ResultSet/ResultSet.h"
#include "./ResultSet/Result.h"

class ResultSet;

class HashMap
{

//private:
public:
	int split_index;
	int original_size, size;
	int round;
	int bucket_cells; //number of cells per bucket at start
	GenArray* hashTable;

	int hash(int );
	int next_hash(int );

	bool insert_into_array(Node*,GenArray*);
	bool split();
	bool isSorted;

public:
    void sort_map();
	bool insertEdge(int id, Edge * insEdge);
	Node * lookupNode(int );
	HashMap(int start_size,int bucket_cells);
	~HashMap();
	bool insertNode(Node* );
	void print();
	ResultSet* reachNodesN(int);
	int reachNode1(int,int);
};

#endif
