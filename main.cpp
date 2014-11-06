#include <iostream>
#include "HashMap/HashMap.h"
#include "list/list.h"

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



    xartis->print();


    komvos = new Node(11);
    xartis->insertNode(komvos);
komvos = new Node(4);
    xartis->insertNode(komvos);
    xartis->print();


	//list* liiiiist = new list();
}
