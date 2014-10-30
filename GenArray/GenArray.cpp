#include "GenArray.h"
#include <stdlib.h>

using namespace std;

GenArray::GenArray(int s) : size(s)
{

	currentSize = s;

	arr = (void **) malloc(size * sizeof(void*));
	for (int i = 0; i < size; i++)
	{
		arr[i] = NULL;
	}
}
GenArray::~GenArray()
{
	for (int i = 0; i < size; i++)
	{
		arr[i] = NULL;
	}
	delete arr;
}

bool GenArray::doubleCells()
{
	arr = (void **) realloc(arr, 2 * currentSize * sizeof(void*));
	currentSize = 2 * currentSize;
	if (arr != NULL)
		return 1;
	else
		return 0;
}

bool GenArray::addCell()
{

	arr = (void **) realloc(arr, (++currentSize * sizeof(void*)) );
	
	if ( arr != NULL )
		return 1;
	else
		return 0;

}

int GenArray::getSize()
{
	return currentSize;
}

int GenArray::fillIt()
{
	int i = 0;
	for( i = 0 ; i < currentSize ; i++ )
	{
		int k = 500;
		arr[i] = &k;
	}
	return *(int*) (arr[currentSize-1]);
}



