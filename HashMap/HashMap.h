#include "../GenArray/GenArray.h"

class HashMap
{

private:
	int split_index;
	int original_size;
	int round;
	GenArray* hashTable;
	
	int hash(int );
	int next_hash(int );
	
public:
	HashMap(int start_size);
	HashMap();
	bool addEntry();
};
