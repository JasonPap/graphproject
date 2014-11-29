#ifndef FLOYD_H
#define FLOYD_H

void floydWarshall(HashMap * hMap, int ** dist, int** next);
list * getFloydPath(int ** next,int from, int to);

#endif