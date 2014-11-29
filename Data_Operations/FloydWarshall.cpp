#include <limits>
#include "FloydWarshall.h"
#include "../HashMap/HashMap.h"

using namespace std;

void floydWarshall(HashMap * hMap, int ** dist, int** next)
{
    int numOfNodes = hMap->getNumOfNodes();

    dist = new int*[numOfNodes];
    next = new int*[numOfNodes];

    for( int i = 0 ; i < numOfNodes ; i++ )
    {
        dist[i] = new int[numOfNodes];
        next[i] = new int[numOfNodes];
    }
    for( int i = 0 ; i < numOfNodes ; i++ )
    {
        for( int j = 0 ; j < numOfNodes ; j++ )
        {
            dist[i][j] = numeric_limits<int>::max();
            next[i][j] = null;
        }
    }

    int* node_IDs = getAllNodeIds();
    for(i=0 ; i<numOfNodes ; i++)
    {
        ///komvos arxis tis akmis node_IDs[i]
        Node* node = lookupNode(node_IDs[i]);
        if(node->links->isEmpty())
            continue;

        listIterator* it = node->links->getIterator();
        do
        {
            ///komvos telous tis akmis destination_id
            int destination_id = ((Edge*)it->getData())->edge_end;

            dist[node_IDs[i]][destination_id] = 1;
            next[node_IDs[i]][destination_id] = destination_id;

        }
        while(it->next()!=NULL);
        delete(it);

    }

    for(int k = 0 ; k < numOfNodes ; k++ )
    {
        for( int i = 0 ; i < numOfNodes ; i++ )
        {
            for( int j = 0 ; j < numOfNodes ; j++ )
            {
                if( (dist[i][k] + dist[k][j]) < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    next[i][j] = next[i][k];
                }
            }
        }
    }
    delete node_IDs;

}

list * getFloydPath(int ** next,int from, int to)
{
    list * path = new list();

    if( next[from][to] == null )
    {
        return path;
    }

    path.Add(from);
    while(to != from)
    {
        from = next[from][to];
        path.Add(from);
    }

    listIterator * li = path->getIterator();

    list * pathR = new list();
    do
    {
        pathR->Add(li->getData());
    }while( li->next() != null);

    delete path;

    return pathR;
}