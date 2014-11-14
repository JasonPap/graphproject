#include <iostream>
#include "HashMap/HashMap.h"
#include "list/list.h"
#include "Edge/Edge.h"
#include "HashMap/ResultSet/ResultSet.h"
#include "HashMap/ResultSet/Result.h"

using namespace std;

int main(void)
{

    if (true)
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

	for(int i  = 10000; i>100; i--)
	{
		komvos = new Node(i);
        	xartis->insertNode(komvos);
	}
	cout << "round = "<<xartis->round<<endl;
        //xartis->print();




        cout<<endl<<"size "<<xartis->hashTable->getSize()<<endl;
        xartis->sort_map();

        Edge* e = new Edge(1,NULL);
        xartis->insertEdge(11,e);

        e = new Edge(12,NULL);
        xartis->insertEdge(1,e);

        e = new Edge(3,NULL);
        xartis->insertEdge(12,e);

        e = new Edge(19,NULL);
        xartis->insertEdge(3,e);

        e = new Edge(19,NULL);
        xartis->insertEdge(1,e);

        //cout<<"h apostasi einai: "<<xartis->reachNode1(1,19);

        ResultSet* r = xartis->reachNodesN(11);
        while(true)
        {
            Result* result = r->get_next();
            if(result != NULL)
            {
                cout<< result->node_id << "   "<<result->distance<<endl;
                delete result;
            }
            else
                break;
        }
        delete(r);

        //result = r->get_next();
        //result->print();

        cout<<endl;

        //xartis->print();

        delete xartis;

    }
    else
    {
        list* l = new list();
        Node* komvos = new Node(1);
        l->Add(komvos);
        listIterator* it = l->getIterator();
        Node* n = (Node*)it->getData();
        cout<<n->get_id()<<endl;

    }
	//list* liiiiist = new list();
}
