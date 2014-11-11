#include <iostream>
#include "HashMap/HashMap.h"
#include "list/list.h"
#include "Edge/Edge.h"
#include "HashMap/ResultSet/ResultSet.h"
#include "HashMap/ResultSet/Result.h"

using namespace std;

int main(void)
{
	int i;
	HashMap* xartis = new HashMap(4,4);
    cout << "split_index = "<<xartis->split_index<<endl;
    cout << "original_size = "<<xartis->original_size<<endl;
    cout << "round = "<<xartis->round<<endl;
    cout << "bucket_cells = "<<xartis->bucket_cells<<endl;

    Node* komvos;
    
    for( i = 99 ; i > 0 ; i-- )
    {
		komvos = new Node(i);
		xartis->insertNode(komvos);
	}
	
    //xartis->print();

	
    
    xartis->sort_map();

	cout << "split_index = "<<xartis->split_index<<endl;
    cout << "original_size = "<<xartis->original_size<<endl;
    cout << "round = "<<xartis->round<<endl;
    cout<<"Num of bucekts = " << xartis->hashTable->getSize() << endl;
    
    /*Edge* e = new Edge(1,NULL);
    xartis->insertEdge(11,e);

    ResultSet* r = xartis->reachNodesN(11);
    Result* result = r->get_next();
    result->print();

    cout<<endl;*/

    //xartis->print();

	cout << "split_index = "<<xartis->split_index<<endl;
    cout << "original_size = "<<xartis->original_size<<endl;
    cout << "round = "<<xartis->round<<endl;
    cout<<"Num of bucekts = " << xartis->hashTable->getSize() << endl;

	//list* liiiiist = new list();
}
