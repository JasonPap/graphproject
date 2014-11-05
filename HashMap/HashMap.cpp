#include <iostream>
#include "HashMap.h"

using namespace std;

HashMap::HashMap(int start_size, int _bucket_cells)
{
	hashTable = new GenArray(start_size);
	for (int i = 0; i < start_size; i++)
	{

		hashTable->arrayPtr[i] = new GenArray(_bucket_cells);

	}
	split_index = 0;
	round = 0;
	original_size = start_size;
	bucket_cells = _bucket_cells;
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
	//if(!(hashTable->arrayPtr[bucket_num])->isFull())
	//{
	//if not
	//	return insert_to_array(new_node,hashTable->arrayPtr[bucket_num]);
	//
	//}
	//if bucket is full
	//increase size of bucket
	//hashTable->arrayPtr[bucket_num]->doubleCells();
	//if(!insert_to_array(new_node,hashTable->arrayPtr[bucket_num]))
    //    cout<<"Errrrrrrrrrrrrrrroorrrr"<<endl;
    if(insert_into_array(new_node,hashTable->arrayPtr[bucket_num]))
    {
        split();
    }

	////.....
}

bool HashMap::split()
{
    hashTable->addCell();
    GenArray* newBucket = new GenArray(bucket_cells);

    hashTable->arrayPtr[hashTable->getSize()-1] = newBucket;

    ///bucket <- p
    ///newBucket empty

    ///newOldBucket

    GenArray* p_bucket = new GenArray(bucket_cells);

    GenArray* bucket_to_split = hashTable->arrayPtr[split_index];

    for(int i = 0; i < bucket_to_split->getNumOfItems(); i++)
    {
        if(next_hash(bucket_to_split->arrayPtr[i]->get_id()) != split_index)
        {
            insert_into_array(bucket_to_split->arrayPtr[i],newBucket);
        }
        else
        {
            insert_into_array(bucket_to_split->arrayPtr[i],p_bucket);
        }
    }

    delete bucket_to_split;
    hashTable->arrayPtr[split_index] = p_bucket;

    split_index++;
    if(split_index > original_size)
    {
        original_size = original_size * 2;
        split_index = 0;
        round++;
    }


}

bool HashMap::insert_to_array(Node* new_node, GenArray* _array)
{
    bool doubled;
    if(_array->isFull())
    {
        _array->doubleCells();
        doubled = true;
    }
    else
    {
        doubled = false;
    }

    _array->arrayPtr[num_of_items] = new_node;
    _array->num_of_items++;
    return doubled;
}

(Node*) HashMap::lookupNode(int idSearched)
{
	int bucket_index = hash(idSearched);
	int found = 0;

	if ( bucket_index < split_index)
	{
		bucket_index = next_hash(idSearched);
	}

	GenArray* bucket = hashTable->arrayPtr[bucket_index];
	int num_of_items = bucket->getNumOfItems();
	int min = 0, max = num_of_items - 1;
	int mid = (max + min) / 2;

	// :)

	while (min<=max)
	{

		if ( bucket->arrayPtr[mid]->get_id() == idSearched )
		{
			return bucket->arrayPtr[mid];
		}
		else if (bucket->arrayPtr[mid]->get_id() < idSearched)
		{
			min = mid+1;
			mid = (min + max) / 2;
		}
		else if (bucket->arrayPtr[mid]->get_id() > idSearched)
		{
			max = mid-1;
			mid = (min + max) / 2;
		}

	}
	return null;
}