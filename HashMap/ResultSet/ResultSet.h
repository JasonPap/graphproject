#ifndef RESULTSET_H
#define RESULTSET_H

#include "../../Node/Node.h"
#include "../../list/list.h"
#include "Result.h"
#include "../../Queue/Queue.h"
#include "../HashMap.h"

class HashMap;

class ResultSet
{
private:
    list* visited_nodes;
    Queue* nodes_to_expand;  ///alagh list se fifo queue
    bool contains(list*,int);
    HashMap* hashmap;
public:
    ResultSet(Node*,HashMap*);
    ~ResultSet();
    Result* get_next();
};

#endif //RESULTSET_H
