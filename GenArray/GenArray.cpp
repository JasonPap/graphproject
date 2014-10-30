#include "GenArray.h"
#include <stdlib.h>

using namespace std;

GenArray::GenArray(int s) : size(s)
{

	num_of_items = 0;

	arrayPtr = (void **) malloc(size * sizeof(void*));
	for (int i = 0; i < size; i++)
	{
		arrayPtr[i] = NULL;
	}
}
GenArray::~GenArray()
{
	for (int i = 0; i < size; i++)
	{
		if (arrayPtr[i] != NULL)
			free(arrayPtr[i]);
	}
	free(arrayPtr);
}

bool GenArray::doubleCells()
{
	arrayPtr = (void **) realloc(arrayPtr, 2 * size * sizeof(void*));
	size = 2 * size;
	if ( arrayPtr != NULL )
		return 1;
	else
		return 0;
}

bool GenArray::addCell()
{

	arrayPtr = (void **) realloc(arrayPtr, (++size * sizeof(void*)) );
	
	if ( arrayPtr != NULL )
		return 1;
	else
		return 0;

}

bool GenArray::isFull()
{
	if(num_of_items >= size)
		return true;
	else
		return false;
}

int GenArray::getSize()
{
	return size;
}

int GenArray::fillIt()
{
	int i = 0;
	for( i = 0 ; i < size ; i++ )
	{
		int k = 500;
		arrayPtr[i] = &k;
	}
	return *(int*) (arrayPtr[size-1]);
}



