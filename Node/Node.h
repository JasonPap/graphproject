#include "../GenArray/GenArray.h"
#include "../list/list.h"

class Node
{
	public:
		Node(int);
		~Node();
		int get_id();
	
	private:
		int id;
		void** properties;
		list* links;
}