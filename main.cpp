#include <iostream>
#include "HashMap/HashMap.h"
#include "list/list.h"
#include "Edge/Edge.h"
#include "HashMap/ResultSet/ResultSet.h"
#include "HashMap/ResultSet/Result.h"

using namespace std;

HashMap * createGraph(int, int);
void destroyGraph(HashMap*);
void insertNode(HashMap *, int);
void insertEdge(HashMap *, int, int);
Node * lookupNode(HashMap *, int);

int main(void)
{


        HashMap* xartis = createGraph(4,4);
        
        insertNode(xartis,1);
        insertNode(xartis,15);
        insertNode(xartis,8);
        insertNode(xartis,3);
        insertNode(xartis,7);
        insertNode(xartis,19);
        insertNode(xartis,12);
        insertNode(xartis,11);
        
        //xartis->print();

        xartis->sort_map();

		insertEdge(xartis, 11, 1);
		insertEdge(xartis, 1, 12);
		insertEdge(xartis, 12, 3);
		insertEdge(xartis, 3, 19);
		insertEdge(xartis, 1, 19);

        cout<< endl << endl << "Distance from 1 "<< " to " << " 3 " << " ----> " << xartis->reachNode1(1,3) << endl << endl;
	
		int start = 11;
        ResultSet* r = xartis->reachNodesN(start);
        while(true)
        {
            Result* result = r->get_next();
            if(result != NULL)
            {
                cout<<"Distance from " << start << " to " << result->node_id << " -----> "<<result->distance<<endl;
                delete result;
            }
            else
                break;
        }
        delete(r);
        
        cout<<endl;

        xartis->print();

        destroyGraph(xartis);

	
}

HashMap * createGraph(int buckets, int bucket_size)
{
		HashMap* xartis = new HashMap(buckets,bucket_size);
}
void insertNode(HashMap * xartis,int _id)
{
	 Node* komvos = new Node(_id);
     xartis->insertNode(komvos);
}
void insertEdge(HashMap * xartis, int from, int to)
{
	Edge* e = new Edge(to,NULL);
    xartis->insertEdge(from,e);
}
Node * lookupNode(HashMap * xartis, int _id)
{
	return xartis->lookupNode(_id);
}
void destroyGraph(HashMap * xartis)
{
	delete xartis;
}



