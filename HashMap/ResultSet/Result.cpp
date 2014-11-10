#include <iostream>
#include "Result.h"

using namespace std;

Result::Result(int ID, int Distance)
{
    node_id = ID;
    distance = Distance;
}

void Result::print()
{
    cout<<"id: "<<node_id<<endl;
    cout<<"distance: "<<distance<<endl;
}
