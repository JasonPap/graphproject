#include <iostream>
#include "HashMap.h"
#include "ResultSet/Result.h"
#include <math.h>
#include "../Data_Operations/BinarySearch.h"
#include "../Data_Operations/MergeSort.h"

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
	original_size = size = start_size;
	bucket_cells = _bucket_cells;
	isSorted = false;
	number_of_edges = 0;
	number_of_nodes = 0;
	diameter = -1;
	averagePathLength = 0.0;
}

HashMap::~HashMap()
{
    for (int i = 0; i < size; i++)
	{
		GenArray* row = (GenArray*)hashTable->arrayPtr[i];
		row->Empty();
		delete(row);
	}
	delete(hashTable);
}

int HashMap::hash(int i)
{
	int r = i % (int)( pow(2,round) * original_size );
	return r;
}

int HashMap::next_hash(int i)
{
	int r = i % (int)( pow(2,round + 1) * original_size );
	return r;
}

bool HashMap::insertNode(Node* new_node)
{
    number_of_nodes++;
    isSorted = false;
	int bucket_num = hash(new_node->get_id());
	if (bucket_num < split_index)
		bucket_num = next_hash(new_node->get_id());
    //cout<<"mothafaka"<<endl;
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


    if(insert_into_array(new_node,(GenArray*)hashTable->arrayPtr[bucket_num]))
    {
        split();
    }

	////.....
}

bool HashMap::split()
{
    hashTable->addCell();
	size++;
    GenArray* newBucket = new GenArray(bucket_cells);

    hashTable->arrayPtr[hashTable->getSize()-1] = newBucket;
    hashTable->num_of_items++;
    ///bucket <- p
    ///newBucket empty

    ///newOldBucket

    GenArray* p_bucket = new GenArray(bucket_cells);

    GenArray* bucket_to_split = (GenArray*)hashTable->arrayPtr[split_index];

    for(int i = 0; i < bucket_to_split->getNumOfItems(); i++)
    {
        if(next_hash(((Node*)bucket_to_split->arrayPtr[i])->get_id()) != split_index)
        {
            insert_into_array((Node*)bucket_to_split->arrayPtr[i],newBucket);
        }
        else
        {
            insert_into_array((Node*)bucket_to_split->arrayPtr[i],p_bucket);
        }
    }

    delete bucket_to_split;
    hashTable->arrayPtr[split_index] = p_bucket;

    split_index++;
    if(split_index == ((int)pow(2,round))*original_size)
    {
        //size = size * 2;
        split_index = 0;
        round++;
    }


}

bool HashMap::insert_into_array(Node* new_node, GenArray* _array)
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

    _array->arrayPtr[_array->num_of_items] = new_node;
    //cout<<_array->num_of_items<<endl;
    (_array->num_of_items)++;
    //cout<<_array->num_of_items<<endl;
    return doubled;
}

Node*  HashMap::lookupNode(int idSearched)
{
    if(!isSorted)
        sort_map();

	int bucket_index = hash(idSearched);
	int found = 0;

	if ( bucket_index < split_index)
	{
		bucket_index = next_hash(idSearched);
	}

	GenArray* bucket = (GenArray*) hashTable->arrayPtr[bucket_index];
	int num_of_items = bucket->getNumOfItems();
	int min = 0, max = num_of_items - 1;
	int mid = (max + min) / 2;

	// :)

	while (min<=max)
	{

		if ( ((Node*)bucket->arrayPtr[mid])->get_id() == idSearched )
		{
			return (Node*)bucket->arrayPtr[mid];
		}
		else if (((Node*)bucket->arrayPtr[mid])->get_id() < idSearched)
		{
			min = mid+1;
			mid = (min + max) / 2;
		}
		else if (((Node*)bucket->arrayPtr[mid])->get_id() > idSearched)
		{
			max = mid-1;
			mid = (min + max) / 2;
		}

	}
	return NULL;
}
void HashMap::sort_map()
{
    for( int i = 0; i < hashTable->getSize() ; i++)
    {
        ((GenArray*)hashTable->arrayPtr[i])->merge_sort();
    }
    isSorted = true;
}

void HashMap::print()
{
    for( int i = 0; i < size ; i++)
    {
        cout<<"row["<<i<<"]:  ";
        ((GenArray*)hashTable->arrayPtr[i])->print();
        cout<<endl;
    }
}

bool HashMap::insertEdge(int id, Edge * insEdge)
{
    Node* temp = lookupNode(id);
    if(temp != NULL)
    {
        temp->links->Add(insEdge);
        number_of_edges++;
        return true;
    }
    else
        return false;

}

ResultSet* HashMap::reachNodesN(int id)
{
    Node* n = lookupNode(id);
    if(n == NULL)
        return NULL;
    ResultSet* return_set = new ResultSet(n,this);
    return return_set;
}

int HashMap::reachNode1(int from,int to)
{
    int d = -1;
    Node* from_node = lookupNode(from);
    ResultSet* distances = new ResultSet(from_node,this);
    bool notfound = true;
    Result* r;

    while(notfound)
    {
        r = distances->get_next();
        if(r == NULL)
        {
            delete(r);
            break;
        }

        if(r->node_id == to)
        {
            d = r->distance;
            notfound = false;
        }

        delete(r);
    }
    delete(distances);
    return d;
}

void HashMap::degreeDistribution()
{
    int degree_array[2][number_of_nodes];
    int z = 0;
    //int
    for(int i = 0; i< number_of_nodes; i++)
    {
        degree_array[1][i] = 0;
    }

    for(int i =0; i < size; i++)
    {
        for(int j=0; j < ((GenArray*)hashTable->arrayPtr[i])->getNumOfItems(); j++)
        {
            degree_array[0][z] = ((Node*)((GenArray*)hashTable->arrayPtr[i])->arrayPtr[j])->get_id();
            z++;
        }
    }

    MergeSort(degree_array[0],number_of_nodes);

    for(int i = 0; i< number_of_nodes; i++)
    {
        Node* n = lookupNode(degree_array[0][i]);
        if(n->links->isEmpty())
            continue;

        listIterator* lit = n->links->getIterator();
        do
        {
            int link_id = ((Node*)lit->getData())->get_id();
            degree_array[1][i]++;
            int index = binarySearch(degree_array[0],number_of_nodes,link_id);
            degree_array[1][index]++;
        }
        while(lit->next()!=NULL);
        delete(lit);
    }
    //#summon Gnu Plot Spirit
}

int* HashMap::getAllNodeIds()
{
	int i,j;
	int z = 0;

	int* result = new int[number_of_nodes];

	for (i = 0; i < size ; i++)
	{
		for (j = 0; j < ((GenArray*)hashTable->arrayPtr[i])->getNumOfItems(); j++)
		{
			result[z] = ((Node*)((GenArray*)hashTable->arrayPtr[i])->arrayPtr[j])->get_id();
			z++;
		}
	}

	return result;
}

int HashMap::Diameter()
{
    if(diameter == -1)
        AveragePathLength();

    return diameter;
}

double HashMap::AveragePathLength()
{
    int max_distance = 0;
    int* node_IDs = getAllNodeIds();

    int sumOfDistances;
    int numOfPaths;

    for(int i = 0; i < number_of_nodes; i++)
    {
        ResultSet* results = reachNodesN(node_IDs[i]);

        while(true)
        {
            Result* result = results->get_next();
            if(result != NULL)
            {
                //cout<<"Distance from " << start << " to " << result->node_id << " -----> "<<result->distance<<endl;
                sumOfDistances += result->distance;
                numOfPaths++;

                if(result->distance > max_distance)
                    max_distance = result->distance;

                delete result;
            }
            else
                break;
        }
        delete(results);
    }

    diameter = max_distance;

    averagePathLength = (double)sumOfDistances/(double)numOfPaths;
    delete(node_IDs);

    return averagePathLength;
}

int HashMap::numberOfCCs()
{
    int connectedComponents = 0;
    int* node_IDs = getAllNodeIds();
    MergeSort(node_IDs,number_of_nodes);
    bool* visited = new bool[number_of_nodes];

    for(int i = 0; i < number_of_nodes; i++)
    {
        visited[i] = false;
    }

    for(int i = 0; i < number_of_nodes; i++)
    {
        if(visited[i] == false)
        {
            FindCC(visited,i,node_IDs);
            connectedComponents++;
        }
    }

    delete(node_IDs);
    delete(visited);
    return connectedComponents;
}

int HashMap::FindCC(bool* visited,int index,int* node_IDs)
{
    int CCsize = 0;
    ResultSet* results = reachNodesN(node_IDs[index]);
    visited[index] = true;
    Result* result;

    while((result = results->get_next()) != NULL)
    {
        int visited_node_id = result->node_id;
        int index = binarySearch(node_IDs,number_of_nodes,visited_node_id);
        visited[index] = true;
        CCsize++;
        delete(result);
    }
    delete(results);
    return CCsize;
}

int HashMap::maxCC()
{
    int maxConnectedComponent = 0;

    int* node_IDs = getAllNodeIds();
    MergeSort(node_IDs,number_of_nodes);
    bool* visited = new bool[number_of_nodes];

    for(int i = 0; i < number_of_nodes; i++)
    {
        visited[i] = false;
    }

    for(int i = 0; i < number_of_nodes; i++)
    {
        if(visited[i] == false)
        {
            int x = FindCC(visited,i,node_IDs);
            if(x  > maxConnectedComponent)
                maxConnectedComponent = x;
        }
    }

    delete(node_IDs);
    delete(visited);
    return maxConnectedComponent;
}

double HashMap::density()
{
    return (double)(2*(double)number_of_edges)/((double)number_of_nodes * ((double)(number_of_nodes - 1)));
}

double HashMap::closenessCentrality(Node* n)
{
    ResultSet* results = reachNodesN(n->get_id());
    double total = 0;
    Result* result;
    while((result = results->get_next() )!= NULL)
    {
        total += 1/result->distance;
        delete(result);
    }
    total = total/(number_of_nodes-1);
    return total;
}


