#include <iostream>
#include "list.h"
#include "listIterator.h"

using namespace std;

class yolo
{
public:
    yolo(int n){num = n;}
    int num;
};


int main(void)
{
    list* test = new list();
    yolo* y1 = new yolo(1);
    yolo* y2 = new yolo(2);

    test->Add(y1);
    test->Add(y2);
    listIterator* iteratorr = test->getIterator();
    cout << "length = " << test->getLength()<<endl;
    cout << test->isEmpty()<<endl;


    yolo* y3 = (yolo*)iteratorr->getData();
    cout << y3->num <<endl;
    iteratorr->next();
    y3 = (yolo*)iteratorr->getData();
    cout << y3->num <<endl;

    return 0;
}
