#include <iostream>
#include "HashMap.h"

using namespace std;

HashMap::HashMap(int start_size) 
{
	split_index = 0;
	round = 0; 
	original_size = start_size;
}

HashMap::HashMap()
{
 cout<<"THIS IS BULLSHIT"<<endl;
}
