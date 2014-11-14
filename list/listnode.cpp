#include <iostream>
#include "listnode.h"


listnode::listnode(void* Data)
{
	data = Data;
	next = NULL;
}


listnode::~listnode()
{
    delete data;
}

void* listnode::GetValue()
{
	return data;
}
