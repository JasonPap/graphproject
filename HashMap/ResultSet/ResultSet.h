#ifndef RESULTSET_H
#define RESULTSET_H

#include "../../Node/Node.h"
#include "../../list/list.h"
#include "Result.h"
#include "../../Queue/Queue.h"


class ResultSet
{
private:
    list* visited_nodes;
    Queue* nodes_to_expand;  ///alagh list se fifo queue
    bool contains(list*,int);
public:
    ResultSet(Node*);
    ~ResultSet();
    Result* get_next();
};

#endif //RESULTSET_H
