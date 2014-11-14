#include "GenArray.h"
#include "../Node/Node.h"
#include <stdlib.h>
#include <iostream>

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
	/*for (int i = 0; i < size; i++)
	{
		if (arrayPtr[i] != NULL)
			free(arrayPtr[i]);
	}*/
	if(arrayPtr!=NULL)
        free(arrayPtr);
}

void GenArray::Empty()
{
    for(int i = 0; i< num_of_items; i++)
    {
        Node* node_to_delete = (Node*)arrayPtr[i];
        delete(node_to_delete);
    }
    num_of_items = 0;
}

bool GenArray::doubleCells()
{
	arrayPtr = (void **) realloc(arrayPtr, 2 * size * sizeof(void*));
	size = 2 * size;
	if ( arrayPtr != NULL )
		return true;
	else
		return false;
}

bool GenArray::addCell()
{

	arrayPtr = (void **) realloc(arrayPtr, (++size * sizeof(void*)) );
	
	if ( arrayPtr != NULL )
		return true;
	else
		return false;

}

bool GenArray::isFull()
{
	if(num_of_items >= size)
		return true;
	else
		return false;
}

int GenArray::getNumOfItems()
{
    return num_of_items;
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

void GenArray::merge_sort()
{
    int n = num_of_items;
    void** help_array = (void **) malloc(n * sizeof(void*));
    TopDownSplitMerge(arrayPtr, 0, n, help_array);
    free(help_array);
}

void GenArray::CopyArray(void* B[], int iBegin, int iEnd, void* A[])
{
    for(int k = iBegin; k < iEnd; k++)
        A[k] = B[k];
}

// iBegin is inclusive; iEnd is exclusive (A[iEnd] is not in the set)
void GenArray::TopDownSplitMerge(void* A[],int iBegin, int iEnd, void* B[])
{
    if(iEnd - iBegin < 2)                       // if run size == 1
        return;                                 //   consider it sorted
    // recursively split runs into two halves until run size == 1,
    // then merge them and return back up the call chain
    int iMiddle = (iEnd + iBegin) / 2;              // iMiddle = mid point
    TopDownSplitMerge(A, iBegin,  iMiddle, B);  // split / merge left  half
    TopDownSplitMerge(A, iMiddle,    iEnd, B);  // split / merge right half
    TopDownMerge(A, iBegin, iMiddle, iEnd, B);  // merge the two half runs
    CopyArray(B, iBegin, iEnd, A);              // copy the merged runs back to A
}

//  left half is A[iBegin :iMiddle-1]
// right half is A[iMiddle:iEnd-1   ]
void GenArray::TopDownMerge(void* A[], int iBegin, int iMiddle, int iEnd, void* B[])
{
    int i0 = iBegin, i1 = iMiddle;

    // While there are elements in the left or right runs
    for (int j = iBegin; j < iEnd; j++)
    {
        // If left run head exists and is <= existing right run head.
        if (i0 < iMiddle && (i1 >= iEnd || ((Node*)A[i0])->id <= ((Node*)A[i1])->id))
        {
            B[j] = A[i0];
            i0 = i0 + 1;
        }
        else
        {
            B[j] = A[i1];
            i1 = i1 + 1;
        }
    }

}

void GenArray::print()
{
    for(int i = 0; i < num_of_items ; i++)
    {
        cout<<((Node*)arrayPtr[i])->get_id()<<"  ";
    }
}
