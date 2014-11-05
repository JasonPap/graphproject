#ifndef NODE_H
#define NODE_H


#include "../GenArray/GenArray.h"
#include "../list/list.h"

class Node
{
	public:
		Node(int);
		~Node();
		int get_id();

		int id;
		void** properties;
		list* links;
};

#endif // NODE_H
