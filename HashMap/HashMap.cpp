#include <iostream>
#include "HashMap.h"

using namespace std;

HashMap::HashMap(int start_size) 
{
	split_index = 0;
	round = 0; 
	original_size = start_size;
}

HashMap::HashMap()
{
 cout<<"THIS IS BULLSHIT"<<endl;
}

int HashMap::hash(int i)
{
	int r = i % ( pow(2,round) * original_size );
	return r;
}

int HashMap::next_hash(int i)
{
	int r = i % ( pow(2,round + 1) * original_size );
	return r;
}

bool HashMap::insertNode(Node* new_node)
{
	int bucket_num = hash(new_node->get_id());
	
	//check if bucket is full
	//if not
	//insert_to_array(new_node,hashTable->array[bucket_num]);
	//
	//if bucket is full
	////split()
	////.....
}