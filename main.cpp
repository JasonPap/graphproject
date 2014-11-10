#include <iostream>
#include "HashMap/HashMap.h"
#include "list/list.h"
#include "Edge/Edge.h"
#include "HashMap/ResultSet/ResultSet.h"
#include "HashMap/ResultSet/Result.h"

using namespace std;

int main(void)
{

	HashMap* xartis = new HashMap(4,4);
    cout << "split_index = "<<xartis->split_index<<endl;
    cout << "original_size = "<<xartis->original_size<<endl;
    cout << "round = "<<xartis->round<<endl;
    cout << "bucket_cells = "<<xartis->bucket_cells<<endl;

    Node* komvos = new Node(1);
    xartis->insertNode(komvos);
    komvos = new Node(15);
    xartis->insertNode(komvos);
    komvos = new Node(8);
    xartis->insertNode(komvos);
    komvos = new Node(3);
    xartis->insertNode(komvos);
    komvos = new Node(7);
    xartis->insertNode(komvos);
    komvos = new Node(19);
    xartis->insertNode(komvos);
    komvos = new Node(12);
    xartis->insertNode(komvos);

    komvos = new Node(11);
    xartis->insertNode(komvos);

    xartis->print();




    cout<<xartis->hashTable->getNumOfItems()<<endl;
    xartis->sort_map();

    Edge* e = new Edge(1,NULL);
    xartis->insertEdge(11,e);

    ResultSet* r = xartis->reachNodesN(11);
    Result* result = r->get_next();
    result->print();

    cout<<endl;

    xartis->print();


	//list* liiiiist = new list();
}
